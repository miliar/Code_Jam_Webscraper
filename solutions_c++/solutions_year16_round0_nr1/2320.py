#include <fstream>
#include <thread>
#include <future>
#include <list>
#include <iostream>
#include <set>

using namespace std;

struct input_data
{
  int64_t n;
  void read(ifstream & input)
  {
    input >> n;
  }
};

struct output_data
{
  int64_t n;
  void write(ofstream & output)
  {
    if (n == 0)
    {
      output << "INSOMNIA";
      return;
    }
    output << n;
  }
};

void add(set<int> & st, long long n)
{
  while (n)
  {
    st.insert(n%10);
    n/=10;
  }
}

output_data calc(input_data d)
{
  if (d.n == 0)
    return {0};
  set<int> digits;
  long long cur = 0;
  while (digits.size() < 10)
  {
    cur += d.n;
    add(digits, cur);
  }
  return {cur};
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
