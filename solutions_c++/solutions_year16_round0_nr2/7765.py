
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

void solve(unsigned int length)
{
	unsigned int ans;
	unsigned int i;

	ans = arr[length - 1] == '-' ? 1 : 0;

	for ( i = 0; i < length-1; i++)
	{
		if (arr[i] != arr[i+1])
		{
			ans++;
		}
	}
	
	fout<<ans<<endl;
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

	fin >> numOfTests;


	for (i = 0; i<numOfTests; i++)
	{
		memset(arr, 0, sizeof(arr));
		fin>> arr;
		for (j = 0; arr[j]; j++)
		{

		}
		fout << "Case #"<<i+1<<": ";
		solve(j);
	}
}
