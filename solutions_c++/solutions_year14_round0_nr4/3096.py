#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <string>

#define SQR(_x) ((_x)*(_x))
//#define REP(_i,_n) for(int _i = 0; _i < (int)(_n); _i++)
//#define FOR(_i,_a,_b) for(int _i = (int)(_a); _i <= (int)(_b); _i++)
//#define BCK(_i,_a,_b) for(int _i = (int)(_a); _i >= (int)(_b); _i--)
#define NL printf("\n")
#define LL long long
#define INF 1000000000

using namespace std;

double x[2][2000]={};

int main()
{
	int n,t;
	int dw,w;
	int a,b;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cin >> n;
		for(int j = 0; j < 2; j++)
		{
			for(int k = 0; k < n; k++)
				scanf("%lf",&x[j][k]);
			sort(x[j],x[j]+n);
		}
		dw = 0;
		w = n;
		a = 0;
		b = 0;
		while(a<n or b<n)
		{
			if(a==n)
				b++;
			else if(b==n)
				a++;
			else
			{
				if(x[0][a]>x[1][b])
				{
					a++;
					b++;
					dw++;
				}
				else
					a++;
			}
		}
		a = 0;
		b = 0;
		while(a<n or b<n)
		{
			if(a==n)
				b++;
			else if(b==n)
				a++;
			else
			{
				if(x[0][a]<x[1][b])
				{
					a++;
					b++;
					w--;
				}
				else
					b++;
			}
		}
		printf("Case #%d: %d %d\n",i,dw,w);
	}
	return 0;
}