#include <fstream>
#include <thread>
#include <future>
#include <list>
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

struct input_data
{
  vector<pair<string, string>> d;
  void read(ifstream & input)
  {
    int n;
    input >> n;
    d.resize(n);
    while (n--)
    {
      input >> d[n].first >> d[n].second;
    }
  }
};

struct output_data
{
  int64_t n;
  void write(ofstream & output)
  {
    output << n;
  }
};

output_data calc(input_data d)
{
  unordered_multiset<string> first;
  unordered_multiset<string> second;
  int bits = d.d.size();
  int last_code = 0;
  int result = 0;
  for (int iter = 0; iter < (1<<bits); ++iter)
  {
    int new_code = iter ^ (iter >> 1);
    for (int bit = 0; bit < bits; ++bit)
    {
      if ((last_code & (1<<bit)) != (new_code & (1<<bit)))
      {
        if (new_code & (1<<bit))
        {
          first.insert(d.d[bit].first);
          second.insert(d.d[bit].second);
        }
        else
        {
          first.erase(first.find(d.d[bit].first));
          second.erase(second.find(d.d[bit].second));
        }
      }
    }
    int cnt = 0;
    int good = true;
    for (int bit = 0; bit < bits && good; ++bit)
    {
      if (!(new_code & (1<<bit)))
      {
        if (first.count(d.d[bit].first) && second.count(d.d[bit].second))
          cnt++;
        else 
          good = false;
      }
    }
    if (good)
      result = max(result, cnt);
    last_code = new_code;
  }
  return {result};
}

const bool multithread = false;

int main(int argc, char **argv) {
  ios::sync_with_stdio(false);
  string input_file = argv[1];
  string output_file = argv[2];
  ifstream input(input_file);
  ofstream output(output_file);
  int total;
  input >> total;

  list<future<output_data>> tasks;
  for (int current = 0; current < total; ++current)
  {
    input_data data;
    data.read(input);
    if (multithread)
    {
      tasks.push_back(
        std::async(
          [data = std::move(data)]()
          {
            return calc(std::move(data));
          }));
    }
    else
    {
      auto result = calc(std::move(data));
      tasks.push_back(
        std::async(
          [result = std::move(result)]()
          {
            return result;
          }));
    }
  }
  int index = 1;
  for (auto & task : tasks)
  {
    std::cout<< index << "\n";
    output << "Case #" << index++ << ": ";  
    task.get().write(output);
    output << "\n";
  }
  return 0;
}