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
  int total;
  std::vector<int> numbers;
  void read(ifstream & input)
  {
    input >> total;
    for (int i=0;i<total;i++)
    {
      int a;
      input >> a;
      numbers.push_back(a);
    }
  }
};

struct output_data
{
  std::vector<std::string> res;
  void write(ofstream & output)
  {
    for (auto & str : res)
      output << str << ' ';
  }
};

struct S
{
  int cnt;
  char c;
  bool operator<( const S & other) const
  {
    return cnt < other.cnt;
  }
};
  
output_data calc(input_data data)
{
  priority_queue<S> queue;
  int total_cnt = 0;
  for (char c = 'A' ; c < 'A' + data.total; ++c)
  {
    queue.push({data.numbers[c -'A'], c});
    total_cnt += data.numbers[c -'A'];
  }
  output_data result;
  if (total_cnt & 1)
  {
    auto cur = queue.top();
    queue.pop();
    string str;
    str = cur.c;
    result.res.push_back(str);
    cur.cnt--;
    if (cur.cnt)
      queue.push(cur);
    total_cnt--;
  }
  while (total_cnt)
  {
    static string curs = "";
    curs.clear();
    {
      auto cur = queue.top();
      queue.pop();
      curs += cur.c;
      cur.cnt--;
      if (cur.cnt)
        queue.push(cur);
      total_cnt--;
    }
    {
      auto cur = queue.top();
      queue.pop();
      curs += cur.c;
      cur.cnt--;
      if (cur.cnt)
        queue.push(cur);
      total_cnt--;
    }
    result.res.push_back(curs);
  }
  return result;
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