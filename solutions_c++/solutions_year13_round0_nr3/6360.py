#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

bool is_pal(long long n)
{
  string str = to_string(n);
  string::reverse_iterator rit = str.rbegin();
  string::iterator it = str.begin();
  for (; it != str.end() && rit != str.rend(); it++, rit++)
    if (*it != *rit)
      return false;
  return true;
}

bool is_fair_square(long long n)
{
  long double tmp = sqrt(n);
  if ((long long(tmp) != tmp)
    return false;

  return is_pal(tmp) && is_pal(n);
}

void solve_case(int id)
{
  int min, max, res = 0;
  cin >> min;
  cin >> max;

  for (; min <= max; min++)
    if (is_fair_square(min))
      res++;

  cout << "Case #" << id << ": " << res << endl;
}

int main(void)
{
  int nb_cases;
  cin >> nb_cases;
  cin.get(); // get rid of the newline

  for (int i = 1; i <= nb_cases; i++)
    solve_case(i);

  return 0;
}
