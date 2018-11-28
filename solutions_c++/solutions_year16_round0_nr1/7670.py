
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
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
#include <cstdarg>
#define UINT64 unsigned __int64
using namespace std;
ifstream  fin("b.txt");
ofstream  fout("c.txt");
#define MAX(a,b) (((a) > (b)) ? (a) : (b))

char arr[1000];
unsigned int gTable[10];

bool updateTable(unsigned long long num)
{
	unsigned int i;
	unsigned int count = 0;

	while (num > 0)
	{
		gTable[num % 10] = 1;
		num /= 10;
	}

	for (i = 0; i < 10; i++)
	{
		if (gTable[i])
		{
			count++;
		}
	}

	return count == 10;
}

void solve(unsigned long long num)
{
	unsigned long long ans = 0;
	bool bRes;

	memset(gTable, 0, sizeof(gTable));

	do
	{
		if (num == 0)
		{
			fout << "INSOMNIA" << endl;
			break;
		}

		while (true)
		{
			ans += num;
			bRes = updateTable(ans);
			if (bRes)
			{
				break;
			}
		}

		fout << ans << endl;
	} while (false);

}

int main(void)
{
	unsigned int numOfTests;
	unsigned int i;
	unsigned int j;
	unsigned int m;
	unsigned int total;
	unsigned int d;	
	unsigned int c;
	unsigned int v;	
	unsigned long long num;

	fin >> numOfTests;


	for (i = 0; i<numOfTests; i++)
	{
		fin>> num;
		fout << "Case #"<<i+1<<": ";
		solve(num);
	}
}
