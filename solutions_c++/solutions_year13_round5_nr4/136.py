#include<map>
#include<set>
#include<list>
#include<cmath>
#include<ctime>
#include<queue>
#include<cctype>
#include<cstdio>
#include<string>
#include<cassert>
#include<climits>
#include<cstdlib>
#include<cstring>
#include<numeric>
#include<sstream>
#include<iostream>
#include<typeinfo>
#include<algorithm>
using namespace std;

double f[21][1<<20];


void init(int n)
{
	int mask = 1<<n;
	f[n][0] = 0.0;
	for(int s=1; s<mask; s++)
	{
		double sum = 0.0;
		int last = 0;
		/// 0=X 1=.
		for(int i=n-1; i>=0 && ((s>>i)&1)==0; i--)last++;
		for(int i=0; i<n; i++) if( (s>>i)&1 )
		{
			double tmp = f[n][s-(1<<i)];

			sum += tmp*(last+1) + (n+n-last)*(last+1)/2;
			/*
			for(int j=0;j<=last;j++)
			{
				sum += tmp+(N-j)
			}
			*/
			///
			last = 0;
		}
		else last++;
		f[n][s] = sum/n;
	}
}

char buf[1005];
void solve()
{
	scanf("%s",buf);
	int L = strlen(buf);
	int stat = 0;
	for(int i=0; i<L; i++)
	{
		if(buf[i] == '.')stat+=(1<<i);
	}

	static int cas = 1;
	printf("Case #%d: %.15f\n",cas++,f[L][stat]);

}
int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	for(int i=1;i<=20;i++)
	{
		init(i);
	}
	int _;
	scanf("%d",&_);
	while(_--)solve();
}
