/*
Author: elfness@UESTC
*/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
using namespace std;
typedef long long LL;
const int V=1000100;
int a[V];
LL s[V];
int _,n,p,q,r,S;
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&_);
	for(int ca=1;ca<=_;ca++)
	{
		scanf("%d%d%d%d%d",&n,&p,&q,&r,&S);
		for(int i=0;i<n;i++)
		a[i+1]=(((LL)i*p+q)%r+S);
		s[0]=0;
		for(int i=1;i<=n;i++)s[i]=s[i-1]+a[i];
		LL ret=s[n];
		int p=0;
		for(int i=1;i<=n;i++)
		{
		    while(p<i)p++;
			while(p!=n&&s[p+1]-s[i-1]<=s[n]-s[p])p++;
			LL mx1=max(s[i-1],max(s[n]-s[p],s[p]-s[i-1]));
			LL mx2=max(s[i-1],s[n]-s[i-1]);
			if(p!=n)mx2=max(s[i-1],max(s[p+1]-s[i-1],s[n]-s[p+1]));
			ret=min(ret,min(mx1,mx2));
			//if(n<10)printf("%d %d %lld %lld %lld\n",i,p,ret,mx1,mx2);
		}
		printf("Case #%d: %.12f\n",ca,1.0*(s[n]-ret)/s[n]);
	}
	return 0;
}
