#include <vector>
#include <cassert>
#include <string>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>
#include <cstdio>
#include <map>
#include <cmath>
#include <stack>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)

typedef long long ll;
const int INF=1000000000LL;

char buf[20001];

int solve()
{
	scanf("%s",buf);
	stack<char> s;
	int res=0;
	for(int i=0;buf[i];i++)
	{
		if(!s.empty() && s.top()==buf[i])
		{
			res+=2;
			s.pop();
		}
		else
			s.push(buf[i]);
	}
	int len=s.size();
	return res+max(0,len/2);
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
		printf("Case #%d: %d\n",test,5*solve());
	return 0;
}
