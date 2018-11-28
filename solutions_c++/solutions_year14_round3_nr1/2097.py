#include <iostream>
#include <vector>
#include <cmath>
#include <sstream>
using namespace std;

template<typename IS>
int get_num_cases (IS &is)
{
  string tmp;
  int num_cases;
  is >> num_cases;
  getline (is, tmp);
  return num_cases;
}

int64_t gcd (int64_t u, int64_t v)
{
  // simple cases (termination)
  if (u == v)
    return u;

  if (u == 0)
    return v;

  if (v == 0)
    return u;

  // look for factors of 2
  if (~u & 1) { // u is even
    if (v & 1) // v is odd
      return gcd (u >> 1, v);
    else // both u and v are even
      return gcd (u >> 1, v >> 1) << 1;
  }

  if (~v & 1) // u is odd, v is even
    return gcd (u, v >> 1);

  // reduce larger argument
  if (u > v)
    return gcd ( (u - v) >> 1, v);

  return gcd ( (v - u) >> 1, u);
}

int active_bit (int64_t q)
{
  for (size_t i=0; i<sizeof (int64_t) *8; ++i) {
    if ( (q & (1 << i) ) == q) return i;
  }
  return 0;
}

template<typename OS>
void print_impossible (OS &os, int t)
{
  os << "Case #" << t << ": impossible" << endl;
}


template<typename OS>
void print_case (OS &os, int t, int value)
{
  os << "Case #" << t << ": " << value << endl;
}

int64_t my_stoi (const string &strnum)
{
  stringstream s (strnum);
  int64_t num;
  s >> num;
  return num;
}

template<typename IS, typename OS>
void solve_case (IS &is, OS &os, int t)
{
  string line;

  // Get case data
  getline (is, line);
  istringstream lineparser (line);
  string pstr, qstr;
  getline (lineparser, pstr, '/');
  getline (lineparser, qstr);
  int64_t p = my_stoi (pstr);
  int64_t q = my_stoi (qstr);

  // Check the easy ones
  if (q == 0 || p == 0 ) {
    print_impossible (os, t);
    return;
  }

  // Simplify fraction
  auto common_factor = gcd (p, q);
  p /= common_factor;
  q /= common_factor;

  // Basic test
  if (q == 1) {
    print_case (os, t, 1);
    return;
  }

  // q must be a power of 2
  bool powerOfTwo = (! (q == 0) ) && (! (q & (q - 1) ) );
  if (!powerOfTwo) {
    print_impossible (os, t);
    return;
  }

  // Solution
  int i=2, j=1;
  while(i < q) {
    if(p > q/i) {
      print_case (os, t, j);
      return;
    }
    i*= 2;
    ++j;
  }
  print_case (os, t, j);
}

int main()
{
  const int t = get_num_cases (cin);
  for (int i=0; i<t; ++i) {
    solve_case (cin, cout, i+1);
  }
  return 0;
}
