#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<queue>
#include<list>
#include<stack>
#include<set>
#include<map>
#include<string>
#include<algorithm>

using namespace std;

#pragma comment(linker, "/STACK:1024000000,1024000000")
#define PB push_back
#define MP make_pair

const double pi=2.0*asin(1.0),eps=1e-12;
const int maxn=1100,maxm=1100000,inf=0x3f3f3f3f;

long long a[maxm];
int main()
{

	long long i,j,k,top=0,l,r,ans,t,ca=1;
	char ch[maxn];
	for(i=1;i<=10000009;i++)
	{
		sprintf(ch,"%lld",i*i);
		for(j=0,k=strlen(ch)-1;j<k;j++,k--)
		{
			if(ch[j]!=ch[k])break;
		}
		if(j>=k)
		{
			sprintf(ch,"%lld",i);
			for(j=0,k=strlen(ch)-1;j<k;j++,k--)
			{
				if(ch[j]!=ch[k])break;
			}
			if(j>=k)
			{
				a[top++]=i*i;
			}
		}
	}
	scanf("%lld",&t);
	while(t--)
	{
		scanf("%lld%lld",&l,&r);
		ans=0;
		for(i=0;i<top;i++)
		{
			if(a[i]>=l&&a[i]<=r)
			{
				ans++;
			}
		}
		printf("Case #%lld: %lld\n",ca++,ans);
	}
	return 0;
}

