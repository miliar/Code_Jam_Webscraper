
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

void main2(unsigned int testNum)
{
	unsigned int	i;
	unsigned int	j;
	unsigned int	a;
	unsigned int	b;
	unsigned int	res;

	fin>>a>>b;
	if (a>484)
	{
		res = 0;
	}
	else if (a>121)
	{
		if (b>=484)
		{
			res = 1;
		}
		else
		{
			res = 0;
		}
	}
	else if (a>9)
	{
		if (b>=484)
		{
			res = 2;
		}
		else if(b>=121)
		{
			res = 1;
		}
		else
		{
			res = 0;
		}
	}
	else if (a>4)
	{
		if (b>=484)
		{
			res = 3;
		}
		else if(b>=121)
		{
			res = 2;
		}
		else if(b>=9)
		{
			res = 1;
		}
		else
		{
			res = 0;
		}
	}
	else if (a>1)
	{
		if (b>=484)
		{
			res = 4;
		}
		else if(b>=121)
		{
			res = 3;
		}
		else if(b>=9)
		{
			res = 2;
		}
		else if(b>=4)
		{
			res = 1;
		}
		else
		{
			res = 0;
		}
	}
	else
	{
		if (b>=484)
		{
			res = 5;
		}
		else if(b>=121)
		{
			res = 4;
		}
		else if(b>=9)
		{
			res = 3;
		}
		else if(b>=4)
		{
			res = 2;
		}
		else 
		{
			res = 1;
		}
	}

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
