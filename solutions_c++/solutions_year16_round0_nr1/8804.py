#include <iostream>
#include <fstream>
#include <vector>

long long count_sheeps(long long n)
  {
  if (!n)
    return 0;
  bool digits[10];
  for (long i = 0; i < 10; ++i)
    digits[i] = 0;

  long true_digits = 0;
  for (long long i = 1; i < 100000; ++i)
    {
    long long k = n * i;
    while (k)
      {
      const long long k_mod_10 = k % 10;
      if (!digits[k_mod_10])
        ++true_digits;
      digits[k_mod_10] = true;
      k /= 10;
      }
    if (true_digits == 10)
      return n * i;
    }
  return 0;
  }

int main()
  {
  long n;
  /*
  std::ifstream fin(L"A-large.in");
  std::ofstream fout(L"A-large.out");
  std::istream& in = fin;
  std::ostream& out = fout;
  */
  std::istream& in = std::cin;
  std::ostream& out = std::cout;
  in >> n;
  std::vector<long long> tests(n);
  for (long i = 0; i < n; ++i)
    in >> tests[i];

  for (long i = 0; i < n; ++i)
    {
    out << "Case #" << i+1 << ": ";
    if (!tests[i])
      out << "INSOMNIA" << std::endl;
    else
      out << count_sheeps(tests[i]) << std::endl;
    }

  return 0;
  }