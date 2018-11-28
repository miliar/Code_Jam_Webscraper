#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<queue>
#include<vector>
#include<stack>
#include<set>
#include<cstring>
#include<cassert>
using namespace std;
long long int comb(long long int n,long long int r)
{
	int p[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61};
	int nfac[18],rfac[18],nrfac[18],i,j,curr;
	long long int ans;

	for(i=0;i<18;i++)
	{
		nfac[i]=0;rfac[i]=0;nrfac[i]=0;
		curr=p[i];
		while(n>=curr){nfac[i]=nfac[i]+(n/curr);curr=curr*p[i];}
		
		curr=p[i];
		while(r>=curr){rfac[i]=rfac[i]+(r/curr);curr=curr*p[i];}
	
		curr=p[i];
		while((n-r)>=curr){nrfac[i]=nrfac[i]+((n-r)/curr);curr=curr*p[i];}
	}

	ans=1;
	for(j=0;j<18;j++)
	{
		for(i=0;i<(nfac[j]-rfac[j]-nrfac[j]);i++)
		{
			ans=ans*p[j];
		}
	}

	return ans;
}
int main()
{
	long long int t,comp=0;
	long long m;
	long double x,c,ans,f,ticket,r;
	scanf("%lld",&t);
	while(comp<t)
	{
		comp++;
		scanf("%Lf %Lf %Lf",&c,&f,&x);
		ans=0;
		r=2;
		m=1;
		ticket=x*f-c*f;
		while(ticket-r*c> 0.0000001)
		{
			ans+=c/r;
			r = 2 + m*f;
			m++;
		}
		ans+=x/r;
		printf("Case #%lld: %.7Lf\n",comp,ans);
	}
	return 0;
}
