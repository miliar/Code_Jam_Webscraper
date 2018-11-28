#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <math.h>
#include <sstream>

using namespace std;

bool is_prime(long long int N)
{
  for (long long int i = 2; i*i < N; ++i)
    {
      if(N%i == 0)
	return false;
    }
  return true;
}

long long int get_divisor(long long int N)
{
  for (long long int i = 2; i*i < N; ++i)
    {
      if(N%i == 0)
	return i;
    }
  return -1;
  
}

long long int from_binary_to(long long int binary, long long int base)
{
  long long int place = 0;
  long long int inter = 0;
  while (binary)
  {
    inter = inter + ((binary%2) * pow(base,place++));
    binary /= 2;
  }
  return inter;
}

string binary_rep(long long int N)
{
  stringstream builder;
  while (N)
  {
    builder << N%2;
    N /= 2;
  }
  string str = builder.str();
  return string(str.rbegin(), str.rend());
}

long long int get_next_jam_coin(long long int prev)
{
  while (prev < pow(2, 16))
  {
    long long int flag = true;
    for (long long int i = 2; i < 11; ++i)
    {
      if (is_prime(from_binary_to(prev, i)))
      {
	//cout << binary_rep(prev) << " failed on base " << i
	//     << " with long long interpretation " << from_binary_to(prev, i) << endl;
	flag = false;
	i = 11;
      }
    }
    if (flag)
      break;
    prev += 2;
  }
  cout << binary_rep(prev) << " ";
  for (long long int i = 2; i < 11; ++i)
  {
    cout << get_divisor(from_binary_to(prev, i)) << " ";
  }
  cout << endl;
  return prev + 2;
}

int main()
{
  cout << "Case #1:" << endl;

  long long int prev = pow(2, 15) + 1;
  for (long long int i = 0; i < 50; ++i)
  {
    prev = get_next_jam_coin(prev);
  }

}
