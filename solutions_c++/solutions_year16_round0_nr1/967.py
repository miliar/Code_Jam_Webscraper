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
	int N ;
	cin >> N;
  std::array<int, 10> v;
  std::fill(v.begin(), v.end(), 0);
  int c = 1;
  do {
    int cN = c * N;
    while (cN > 0)
    {
      v[cN % 10]++;
      cN /= 10;
    }
    if (std::find(v.begin(), v.end(), 0) == v.end())
      break;
    else
      c++;
  } while (c < 100);

  if ( c < 100 )
    std::cout << "Case #" << i + 1 << ": " << c * N << std::endl;
  else
    std::cout << "Case #" << i + 1 << ": " << "INSOMNIA" << std::endl;
} 

int main()
{
  int n;
	std::cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		testcase(i);
	}
	
	return 0;
}