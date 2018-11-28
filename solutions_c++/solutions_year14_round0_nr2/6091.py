#pragma comment(linker,"/STACK:102400000,102400000")
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <ctime>
#include <cmath>
#include <cassert>
#include <stack>

#define MP make_pair
#define PB push_back
#define SZ(x) (int)x.size()
#define INF 1<<29
#define pii pair<int,int>
#define pll pair<LL,LL>
#define pdd pair<double,double>
#define vi vector<int>
#define L(x) x<<1
#define R(x) x<<1|1
#if(_WIN32||__WIN32__)
    #define LL __int64
    #define ll I64
#else
    #define LL long long
#endif
//#define Local

using namespace std;

double C,F,X;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T,Case=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%lf %lf %lf",&C,&F,&X);
		double v=2.0;
		double t=0;
		while(X/v>(X)/(F+v)+C/v)
		{
			t+=C/v;
			v+=F;
		}
		printf("Case #%d: %.7lf\n",++Case,t+X/v);
	}
	return 0;
}