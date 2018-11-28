#include <iostream> 
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
int n;
char ts[1002];
void task()
{
	scanf("%d",&n);
	scanf("%s",&ts);
	int tot=0;
	int ans=0;
	rep2(i,0,n)
	{
		ts[i]-='0';
		if(ts[i])
		{
			while(tot<i){++tot;++ans;}
			tot+=ts[i];
		}
	}
	printf("%d\n",ans);
}
int main()
{
	//freopen("in","r",stdin);
	//freopen("out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt)
	{
		printf("Case #%d: ",i);
		task();
	}
}
	
