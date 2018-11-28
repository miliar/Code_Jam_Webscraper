#include <fstream>
#include <thread>
#include <future>
#include <list>
#include <iostream>
#include <set>
#include <sstream>
#include <vector>

using namespace std;

struct input_data
{
  string str;
  void read(ifstream & input)
  {
    input >> str;
  }
};

struct output_data
{
  string n;
  void write(ofstream & output)
  {
    output << n;
  }
};

void decr(
  std::vector<int> &what, int how, const std::string & by)
{
  for (auto c : by)
  {
    what[c] -= how;
  }
}

output_data calc(input_data data)
{
  vector<int> res(10);
  vector<int> cnt(256);
  for (auto s : data.str)
  {
    cnt[s]++;
  }
  res[0] = cnt['Z'];
  decr(cnt, res[0], "ZERO");
  res[6] = cnt['X'];
  decr(cnt, res[6], "SIX");
  res[2] = cnt['W'];
  decr(cnt, res[2], "TWO");
  res[4] = cnt['U'];
  decr(cnt, res[4], "FOUR");
  res[8] = cnt['G'];
  decr(cnt, res[8], "EIGHT");
  res[1] = cnt['O'];
  decr(cnt, res[1], "ONE");
  res[3] = cnt['H'];
  decr(cnt, res[3], "THREE");
  res[5] = cnt['F'];
  decr(cnt, res[5], "FIVE");
  res[7] = cnt['S'];
  decr(cnt, res[7], "SEVEN");
  res[9] = cnt['I'];
  decr(cnt, res[9], "NINE");
  std::stringstream result;
  for (int i = 0; i < 10; ++i)
  {
    while (res[i]--)
    {
      result << char('0' + i);
    }
  }
  return {result.str()};
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