#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;

const int mod=1000002013;
int N;
long long get(long long n,int k)
{
	if(n==0)
		return 0;
	return ((n)*N-(n*(n+1)/2))%mod*k%mod;
}
int sta[110000],p[11000];

struct NN
{
	int kind,p,num;
}nn[11000];

int cmp(NN a,NN b)
{
	if(a.p==b.p)
		return a.kind<b.kind;
	return a.p<b.p;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A1.out","w",stdout);
	int T,ii=0;
	int n,m,i,j,k;

	long long ans=0,ans1;

	cin>>T;
	for(ii=1;ii<=T;ii++)
	{
		cin>>n>>m;
		int o,e;
		N=n;ans=0;
		ans1=0;
		for(i=1;i<=m;i++)
		{
			cin>>o>>e>>j;
			ans1+=get(e-o,j);
			ans1%=mod;
			nn[i].kind=0,nn[i].num=j,nn[i].p=o;
			nn[i+m].kind=1,nn[i+m].num=j,nn[i+m].p=e;
		}
		sort(nn+1,nn+1+m+m,cmp);
		int top=0;

		for(i=1;i<=m+m;i++)
		{
			if(nn[i].kind==0)
			{
				sta[++top]=nn[i].num;
				p[top]=nn[i].p;
			}
			else
			{
				while(nn[i].num)
				{
					j=min(nn[i].num,sta[top]);
					ans+=get(nn[i].p-p[top],j);
					ans%=mod;
					nn[i].num-=j;
					sta[top]-=j;
					if(sta[top]==0)
						top--;
				}
			}
		}
		printf("Case #%d: ",ii);
		cout<<(((ans1-ans)%mod)+mod)%mod<<endl;
	}
}