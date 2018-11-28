#include <fstream>
#include <thread>
#include <future>
#include <list>
#include <iostream>
#include <set>

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
  int64_t n;
  void write(ofstream & output)
  {
    output << n;
  }
};

output_data calc(input_data d)
{
  int swaps = 0;
  char cur = '+';
  for (int index = d.str.size() - 1; index >=0; --index)
  {
    if (cur != d.str[index])
    {
      swaps++;
      cur = d.str[index];
    }
  }
  return {swaps};
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
