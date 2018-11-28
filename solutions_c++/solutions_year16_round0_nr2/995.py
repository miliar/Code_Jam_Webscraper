#include "stdafx.h"

#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <array>

using namespace std;

#define SIZE 1000005

int test(int N)
{
  std::array<int, 10> v;
  std::fill(v.begin(), v.end(), 0);
  bool possible = false;
  int c = 1;
  while ( c < 100 && !possible )
  {
    int cN = c * N;
    while (cN > 0)
    {
      v[cN % 10]++;
      cN /= 10;
    }
    if (std::find(v.begin(), v.end(), 0) == v.end())
      possible = true;
    else
      c++;
  } 

  if (possible)
    std::cout << "Case #" << N << ": " << c << std::endl;
  else
    std::cout << "Case #" << N << ": " << "INSOMNIA" << std::endl;

  return c;
}

void testcase(int i)
{
  string s;
  cin >> s;

  int ch = 0;

  for (int i = 1; i < s.size() && (s[i] == '+' || s[i] == '-'); ++i)
  {
    if (s[i] != s[i - 1])
      ch++;
  }

  int c  = ch % 2 == 0 
           ? s[0] == '+'
             ? ch
             : ch + 1
           : s[0] == '+'
             ? ch + 1
             : ch;
  
  std::cout << "Case #" << i << ": " << c << std::endl;
} 

int main()
{
  int n;
	std::cin >> n;
	
	for (int i = 1; i <= n; i++)
	{
		testcase(i);
	}
	
	return 0;
}