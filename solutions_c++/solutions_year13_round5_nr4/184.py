#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#define pb push_back
#define mp make_pair
#define ST begin()
#define ED end()
#define XX first
#define YY second
#define elif else if 
#define foreach(i,x) for (__typeof((x).ST) i=(x).ST;i!=(x).ED;++i) 
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vci;
typedef vector<string> vcs;
typedef pair<int,int> PII;

const int N = 205;

int n;
int a[N];
char o[N];
double f[1<<21], g[1<<21];

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	int task;
	scanf("%d", &task);
	for (int _i=1;_i<=task;++_i)
	{
		scanf("%s",o);
		n=strlen(o);
		int w=0;
		for (int i=0;i<n;++i)
			a[i]=o[i]=='X',w|=a[i]<<i;
		int m=1<<n;
		for (int i=0;i<m;++i)
			f[i]=-2;
		f[w]=0;
		double u=1./n;
		memset(g, 0, sizeof g);
		g[w]=1;
		/*
		for (int i=0;i<n;++i)
			u/=n;*/
		for (int i=0;i+1<m;++i)
			if (f[i]>-1)
			{
//				printf("f[%d] : %.3lf\n", i, f[i]);
				int ne=0,wa=0,pw=1;
				for (int j=0;j<n;++j)
				{
					while (i&1<<ne)
					{
						++ne;
						ne-=(ne==n)*n;
						++wa;
						pw=wa+1;
					}
					int x=i|1<<ne;
					if (f[x]<-1) f[x]=0;
					f[x]+=f[i]*u+1.*(n-wa)*g[i]*u;
					g[x]+=g[i]*u;
					if (wa)
						--wa;
					else
						pw=1;
					if (j==ne) ++ne;
				}
			}
//		printf("f[%d] : %.3lf\n", m-1, f[m-1]);
		printf("Case #%d: %.10lf\n", _i, f[m-1]/g[m-1]);
	}

	return 0;
}
