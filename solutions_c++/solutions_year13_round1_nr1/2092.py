
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <limits>
#include <iomanip>

using namespace std;
ifstream fin("b.in");
ofstream fout("b.out");

unsigned long long solve(unsigned long long r, unsigned long long t)
{
	unsigned long long i;
	unsigned long long res = 0;
	
	r++;
	while(1)
	{
		if (t>=(2*r-1))
		{
			t-=(2*r-1);
		}
		else
		{
			break;
		}
		res++;
		r+=2;
	}

	return res;
}


void main2(unsigned int testNum)
{
	unsigned int		i;
	unsigned int		j;
	unsigned long long	r;
	unsigned long long	t;
	unsigned long long	res;

	fin>>r>>t;
	res = solve(r,t);

	fout<<"Case #"<<testNum<<": "<<res<<endl;
}

int main(void)
{
	unsigned int numOfTests;
	unsigned int i;

	fin>>numOfTests;
	for(i=0;i<numOfTests;i++)
	{
		main2(i+1);
	}
	return 0;
}
