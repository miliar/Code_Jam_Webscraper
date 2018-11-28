#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<deque>
#include<string> 
#include<iostream>
#include<vector>
#define LL long long
#define INF 0X7FFFFFFF
using namespace std;
int T;
char s[500];
inline void open()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
}
LL num;
int cas=0;
bool flag[11];
inline bool check(LL P)
{
	while(P!=0)
	{
		flag[P%10]=1;
		P/=10;
	}
	for(int i=0;i<10;i++)
	{
		if(!flag[i])
			return 0;
	}
	return 1;
}
int main()
{
	open();
	scanf("%d",&T);
	while(T--)
	{
		scanf("%lld",&num);LL ans=0;bool tag=0;
		memset(flag,0,sizeof(flag));
		for(int i=1;i<=500;i++)
		{
			LL P=i*num;
			if(check(P))
			{
				tag=1;
				ans=P;
				break;
			}
		}
		printf("Case #%d: ",++cas);
		if(tag==0||num==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		cout<<ans<<endl;
	}
	return 0;
}
