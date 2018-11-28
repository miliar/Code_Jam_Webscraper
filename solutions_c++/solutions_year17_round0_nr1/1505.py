#include <fstream>
#include <thread>
#include <future>
#include <list>
#include <iostream>
#include <set>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;

struct input_data
{
  std::string str;
  int k;
  void read(ifstream & input)
  {
    input >> str >> k; 
  }
};

struct output_data
{
  int res;
  void write(ofstream & output)
  {
    if (res==-1)
      output << "IMPOSSIBLE";
    else
      output << res;
  }
};

output_data calc(input_data data)
{
  output_data res;
  res.res = 0;
  for (int i = data.str.size() - 1; i >= data.k - 1; --i)
  {
    if (data.str[i] == '-')
    {
      res.res += 1;
      for (int j = 0; j < data.k; j++)
      {
        data.str[i-j] = (data.str[i-j] == '+' ? '-' : '+');
      }
    }
  }
  if (data.str.find('-') != data.str.npos)
    res.res = -1;
  return res;
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