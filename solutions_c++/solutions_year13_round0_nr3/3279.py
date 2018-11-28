#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int a,b,x,y,t,tt;
string s,ss;

void work()
{
	int ans=0;
	scanf("%d%d",&a,&b);
	for (int i=a;i<=b;++i)
	{
		int v=int( sqrt(i+0.01) );
		if (v*v==i)
		{
			int now=i;
			s="";
			while (now>0)
			{
				s=s+char('0'+now%10);
				now/=10;
			}
			ss=s;
			reverse(s.begin(),s.end());
			if (s==ss) 
			{
				int now=v;
				s="";
				while (now>0)
				{
					s=s+char('0'+now%10);
					now/=10;
				}
				ss=s;
				reverse(s.begin(),s.end());
				if (s==ss) ++ans;
			}
		}
	}
	printf("Case #%d: %d\n",tt,ans);
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);


	scanf("%d",&t);
	for (tt=1;tt<=t;++tt) 
	{
		work();
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
