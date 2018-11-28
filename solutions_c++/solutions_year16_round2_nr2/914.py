#include <fstream>
#include <thread>
#include <future>
#include <list>
#include <iostream>
#include <set>

using namespace std;

struct input_data
{
  string c;
  string j;
  void read(ifstream & input)
  {
    input >> c >> j;
  }
};

struct output_data
{
  string c;
  string j;
  void write(ofstream & output)
  {
    output << c << ' ' << j;
  }
};

bool valid(int a, const std::string & b)
{
  int index = b.size() - 1;
  while (index >= 0)
  {
    if (b[index] != '?' && (b[index] - '0') != a % 10)
      return false;
    a/=10;
    index--;
  }
  return a == 0 && index == -1;
}

string str(int a, string b)
{
  int index = b.size() - 1;
  while (index >= 0)
  {
    if (b[index] == '?')
      b[index] = char(a % 10 + '0');
    a/=10;
    index--;
  }
  return b;
}

output_data calc(input_data d)
{
  int res = 1000;
  string resc;
  string resj;
  for (int i = 0; i <= 999; ++i)
  {
    for (int j = 0; j <= 999; ++j)
    {
      if (!valid(i, d.c) || !valid(j, d.j))
        continue;
      int diff = abs(i-j);
      if (diff < res)
      {
        res = diff;
        resc = str(i, d.c);
        resj = str(j, d.j);
      }
    }
  }
  return {resc, resj};
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