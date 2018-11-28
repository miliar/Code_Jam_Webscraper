#include <fstream>
#include <thread>
#include <future>
#include <list>
#include <iostream>
#include <set>
#include <queue>

using namespace std;

struct input_data
{
  int b,m;
  void read(ifstream & input)
  {
    input >> b >> m;
  }
};

struct output_data
{
  string res;
  void write(ofstream & output)
  {
    output << res;
  }
};

bool test(int k, int mask, int m, string & result)
{
  bool used[6]= {0,0,0,0,0,0};
  int res[6]= {1,0,0,0,0};
  int was[6]= {0,0,0,0,0,0};
  int resb[6] {0,0,0,0,0,0};
  queue<int> q;
  q.push(0);
  while (q.size())
  {
    int cur = q.front();
    q.pop();
    was[cur] = true;
    for (int bit = 0; bit < k; ++bit)
    {
      int cb = cur * k + bit;
      if (!(mask & (1<<cb)))
        continue;
      if (was[bit])
        return false;
      res[bit] += res[cur];
      if (used[bit] == false)
      {
        used[bit] = true;
        q.push(bit);
      }
    }
    resb[cur] = res[cur];
  }
  int total = 0;
  for (int fr = 1; fr <= k; fr ++)
  {
    total += resb[fr - 1];
    if (total == m)
    {
      result = "POSSIBLE\n";
      for (int i = 0; i < k; ++i)
      {
        for (int j = 0; j < k; ++j)
        {
          if (mask & (1 << (i * k + j)))
            result += '1';
          else
            result += '0';
        }
        if (i < fr)
          result += '1';
        else
          result += '0';
        result += '\n';
      }
      result += string(k + 1, '0');
      return true;
    }
  }
  return false;
}

output_data calc(input_data d)
{
  string result = "";
  int k = d.b - 1;
  for (int curm = 0; curm < (1<<(k*k)); ++curm)
  {
    if (test(k, curm, d.m, result))
      return {result};
  }
  return {"IMPOSSIBLE"};
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
    std::cerr << current << '\n';
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
    std::cerr<< index << "\n";
    output << "Case #" << index++ << ": ";  
    task.get().write(output);
    output << "\n";
  }
  return 0;
}