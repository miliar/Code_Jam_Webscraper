#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <cmath>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);i++)

const int MAXN=1001;

int s;
char buf[MAXN];

int solve()
{
	scanf("%d",&s);
	scanf("%s",buf);
	int lo=0;
	int hi=1000;
	while(lo<hi)
	{
		int cu=(lo+hi)/2;
		int cnt=cu;
		bool ok=true;
		for(int i=0;i<=s;i++)
		{
			if(buf[i]!='0')
			{
				if(cnt<i) ok=false;
				cnt+=buf[i]-'0';
			}
		}
		if(ok)
			hi=cu;
		else
			lo=cu+1;
	}
	return lo;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d: %d\n",test,solve());
	}
	return 0;
}
