#include<stdio.h>
#include<string.h>
#include<iostream>
#include<math.h>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
bool ok[10];
void solve(lld s)
{
	while(s>0)
	{
		ok[s%10]=true;
		s/=10;
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A2.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		lld add;
		cin >> add;
		if(add == 0)
		{
			printf("Case #%d: INSOMNIA\n",cc);
			continue;
		}
		memset(ok,false,sizeof(ok));
		lld s=0;
		while(1)
		{
			s+=add;
			solve(s);
			bool flag=true;
			for(int i=0;i<10;i++)
				if(!ok[i])
					flag=false;
			if(flag)
				break;
		}
		printf("Case #%d: %I64d\n",cc,s);
	}
    return 0;
}
/*
5
0
1
2
11
1692

 */
