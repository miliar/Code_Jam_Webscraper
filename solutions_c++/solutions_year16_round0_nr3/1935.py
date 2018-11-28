#include <vector>
#include <fstream>
#include <thread>
#include <future>
#include <list>
#include <iostream>
#include <set>
#include <algorithm>

using namespace std;




struct input_data
{
  int n,j;
  void read(ifstream & input)
  {
    input >> n >> j;
  }
};

struct output_data
{
  vector<long long> result;
  vector<vector<int>> div;
  void write(ofstream & output)
  {
    output << '\n';
    for (int i = 0; i < result.size(); ++i)
    {
      std::string res;
      while (result[i])
      {
        res += '0' + (result[i] & 1);
        result[i] >>= 1;
      }
      reverse(res.begin(), res.end());
      output << res << ' ' ;
      for (const auto cur : div[i])
        output << cur << ' ';
      output << '\n';
    }
  }
};

int findm(int i, int curmask, int n)
{
  int curp = i + 2;
  int res = 2;
  int max_degree = n / 2 + 1;
  long long mx = std::min(1000000ll, (long long)(pow(curp * 1ll, max_degree)));
  while (res <= mx)
  {
    long long sum = 0;
    for (int bit = n-1; bit>=0; --bit)
    {
      sum *= curp;
      sum += (((1<<bit)&curmask) != 0);
      sum = (sum) % res;
    }
    if (sum == 0)
      return res;
    res++;
  }
  return -1;
}

output_data calc(input_data d)
{
  if (d.n <= 3)
    return {};
  int mask = 0;
  std::vector<int> div(9);
  output_data result;
  while (result.result.size() < d.j)
  {
    if ((mask << 1)&(1<<(d.n-1)))
      throw std::runtime_error("Fail :(");
    
    long long curmask = (1 | (mask<<1) | (1ll<<(d.n-1)));
    bool good = true;
    for (int i = 0; i < 9; ++i)
    {
      int curm = findm(i, curmask, d.n);
      if (curm == -1)
      {
        good = false;
        break;
      }
      else
      {
        div[i] = curm;
      }
    }
    if (good)
    {
      cerr << "done " <<  result.result.size() <<"\n";
      result.result.push_back(curmask);
      result.div.push_back(div);
    }
    mask++;
  }
  return result;
}











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
    tasks.push_back(
      std::async(
        launch::async,
        [data = std::move(data)]()
        {
          return calc(std::move(data));
        }));
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
