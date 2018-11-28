#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;
int n,m;
int *gra;
void calculate(int test);
bool worksVer(int i, int j);
bool worksHor(int i, int j);
int main(void)
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int nTest;

	scanf("%d", &nTest);

	for (int i = 0; i < nTest ; i++)
	{
		scanf("%d %d",&n, &m);
		gra = new int[n*m];
		for (int j = 0; j < n ; j++)
		{
			for (int k = 0; k < m ; k++)
			{
				scanf("%d",&(gra[j*m+k]));
			}
		}


		calculate(i+1);



		delete[] gra;

	}
	return 1;
}

void calculate( int test)
{
	bool work;
	for (int i = 0; i < n ; i++)
	{
		for (int j = 0; j < m ; j++)
		{
			if ((!worksHor(i,j)) && (!worksVer(i,j)))
			{
				printf("Case #%d: NO\n",test);
				return;
			}

		}
	}
	printf("Case #%d: YES\n",test);
	return ;
}

bool worksVer( int i, int j )
{
	int tmp = gra[i*m+j];
	for (int ii = 0; ii < n ; ii++)
	{
		if (gra[ii*m + j] >tmp)
		{
			return false;
		}
	}
	return true;
}

bool worksHor( int i, int j )
{
	int tmp = gra[i*m+j];
	for (int ii = 0; ii < m ; ii++)
	{
		if (gra[i*m + ii] >tmp)
		{
			return false;
		}
	}
	return true;
}
