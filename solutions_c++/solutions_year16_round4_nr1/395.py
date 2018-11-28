#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
using namespace std;
//r<p<s r=0,p=1,s=2
int sum[3],n;
char ch[3]={'R','P','S'};
char str1[111111],ans[111111];
bool ans_key;
bool dfs(int l,int r,int now)
{
	if(l==r){
		str1[l]=ch[now];
		return true;
	}
	bool key=true;
	int mid=l+r>>1;
	int d=(now-1+3)%3;
	sum[d]--;
	if(sum[d]>=0)
	key&=dfs(l,mid,d);
	else return false;
	key&=dfs(mid+1,r,now);
	return key;
}
void tz(int l,int r)
{
	int mid=l+r>>1;
	if(l==r)return ;
	tz(l,mid);
	tz(mid+1,r);
	bool big=false;
	for(int i=l,j=mid+1;i<=mid;i++,j++)
	{
		if(str1[i]>str1[j])
		{
			big=true;
			break;
		}
		else if(str1[i]<str1[j])break;
	}
	if(big)
	for(int i=l,j=mid+1;i<=mid;i++,j++)
	{
		swap(str1[i],str1[j]);
	}
}
void solve(int now)
{
	sum[now]--;
	if(sum[now]<0)return;
	if(dfs(1,1<<n,now))
	{
		tz(1,1<<n);
		bool rep=true;
		if(ans_key)
		{
			for(int i=1;i<=(1<<n);i++)
			{
				if(str1[i]>ans[i]){rep=false;break;}
				else if(str1[i]<ans[i])break;
			}
			
		}
		ans_key=true;
		if(rep)for(int i=1;i<=(1<<n);i++)
		{
			ans[i]=str1[i];
		}
	}
	
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,cas=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		int r,p,s;
		scanf("%d%d%d",&r,&p,&s);
		ans_key=false;
		sum[0]=r;
		sum[1]=p;
		sum[2]=s;
		solve(0);
		sum[0]=r;
		sum[1]=p;
		sum[2]=s;
		solve(1);
		sum[0]=r;
		sum[1]=p;
		sum[2]=s;
		solve(2);
		printf("Case #%d: ",++cas);
		if(ans_key)
		{
			for(int i=1;i<=(1<<n);i++)
			printf("%c",ans[i]);
		}
		else{
			printf("IMPOSSIBLE");
		}
		printf("\n");
	}
}