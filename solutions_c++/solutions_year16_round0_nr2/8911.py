#include <iostream>
#include <fstream>
#include <vector>
#include <string>

typedef std::vector<short> TCakes;

long find_minimum(TCakes& cakes, int n)
  {
  if (n == 0)
    return 0;
  
  if (cakes[n - 1] == 1)
    return find_minimum(cakes, n - 1);

  long result = 1;
  for (long i = 1; i < n; ++i)
    if (cakes[i] != cakes[i - 1])
      ++result;

  return result;
  }

int main()
  {
  long n;
  std::ifstream fin(L"B-large.in");
  std::ofstream fout(L"B-large.out");
  std::istream& in = fin;
  std::ostream& out = fout;

  //std::istream& in = std::cin;
  //std::ostream& out = std::cout;
  in >> n;
  std::vector<TCakes> tests(n);
  for (long i = 0; i < n; ++i)
    {
    std::string cake;
    in >> cake;
    tests[i].resize(cake.size(), 0);
    for (size_t c_i = 0; c_i < cake.size(); ++c_i)
      if (cake[c_i] == '+')
        tests[i][c_i] = 1;
    }

  for (long i = 0; i < n; ++i)
    {
    out << "Case #" << i+1 << ": ";
    out << find_minimum(tests[i], tests[i].size()) << std::endl;
    }

  return 0;
  }