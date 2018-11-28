#include <iostream>
#include<iomanip>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <deque>
#define SET(p) memset(p,-1,sizeof(p))
#define CLR(p) memset(p,0,sizeof(p))
#define LL long long int
#define ULL unsigned long long int
#define S(n) scanf("%d",&n)
#define Sl(n) scanf("%lld",&n)
#define Sf(n) scanf("%lf",&n)
#define Ss(n) scanf("%s",n)
using namespace std;
int kmod=1000000007;

void fun(int k)
{
	int n,m;
	S(n);
	S(m);
	int matrix[100][100];
	int *rowMax= new int[n];
	int *colMax= new int[m];

	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
			S(matrix[i][j]);
	}
	//int y;
	for(int i=0;i<n;i++)
	{
		rowMax[i]=matrix[i][0];
		for(int j=1;j<m;j++)
		{
			rowMax[i]=(rowMax[i]<matrix[i][j])?matrix[i][j]:rowMax[i];
		}
	}

	for(int i=0;i<m;i++)
		{
			colMax[i]=matrix[0][i];
			for(int j=1;j<n;j++)
			{
				colMax[i]=(colMax[i]<matrix[j][i])?matrix[j][i]:colMax[i];
			}
		}

	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(matrix[i][j]!=rowMax[i] && matrix[i][j]!=colMax[j])
			{
				printf("Case #%d: NO\n",k);
				return;
			}
		}
	}
	printf("Case #%d: YES\n",k);
}

int main()
{
	int t;
	S(t);
	for(int k=1;k<=t;k++)
	{
		fun(k);
		//cin>>s;
	}
	return 0;
}

