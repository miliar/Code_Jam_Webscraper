#include "test.hh"
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <cmath>

// values:
// 1 : 1
// i : 2
// j : 3
// k : 4
long multiply(long x, long y)
{
  int sign = (x * y < 0) ? -1 : 1;
  x = std::abs(x);
  y = std::abs(y);
  if (x == 1)
    return sign * y;
  if (y == 1)
    return sign * x;
  if (x == y)
    return sign * -1;
  if (x == 2)
  {
    if (y == 3)
      return sign * 4;
    else
      return sign * -3;
  }
  if (x == 3)
  {
    if (y == 2)
      return sign * -4;
    else
      return sign * 2;
  }
  if (y == 2)
    return sign * 3;
  return sign * -2;
}
long get_value(char c)
{
  return c - 'g';
}
long calc_substring(const std::string& real, long start, long end)
{
  long result = 1;
  for (long i = start; i < end; ++i)
    result = multiply(result, get_value(real[i]));

  return result;
}
std::string create_real_string(std::string& str, long repeat)
{
  std::string real = "";
  for (long i = 0; i < repeat; ++i)
    real += str;
  return real;
}
Test::Test(std::string str, long repeat)
     : str_(str)
     , repeat_(repeat)
{}

bool Test::is_possible()
{
  std::string real = create_real_string(str_, repeat_);
  std::cout << "Start size: " << real.size() << std::endl;
  long firsts = 1;
  long seconds = 1;
  long thirds = 1;
  for (unsigned i = 0; i < real.size(); ++i)
  {
    firsts = multiply(firsts, get_value(real[i]));
    if (firsts != 2)
      continue;
    seconds = 1;
    for (unsigned j = i + 1; j < real.size(); ++j)
    {
      seconds = multiply(seconds, get_value(real[j]));
      if (seconds != 3)
        continue;
      thirds = calc_substring(real, j + 1, real.size());
      if (thirds == 4)
        return true;
    }
  }
  return false;
}
