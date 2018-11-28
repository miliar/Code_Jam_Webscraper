#include<stdio.h>
#include<algorithm>
using namespace std;
const int Maxn=1020;
char s[Maxn];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int _,cs=1;scanf("%d",&_);
	while(_--)
	{
		int n;scanf("%d%s",&n,s);
		int cur=0,ans=0;
		for(int i=0;i<=n;i++)
		{
			if(cur<i){ans+=i-cur;cur=i;}
			cur+=s[i]-'0';
		}
		printf("Case #%d: %d\n",cs++,ans);
	}
}
