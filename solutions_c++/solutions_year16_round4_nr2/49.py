#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
int n,nk;
double ind[201];
double tdp[201][201];
bool meet[201];
double calc()
{
	int tn=0;
	memset(tdp,0,sizeof tdp);
	tdp[0][0]=1;
	rep(i,n)
	{
		if(meet[i])
		{
			++tn;
			rep2(k,0,n)
			{
				tdp[tn][k]=tdp[tn-1][k]*(1-ind[i])+(k?tdp[tn-1][k-1]*ind[i]:0);
			}
		}
	}
	assert(tn==nk);
	return tdp[nk][nk/2];
}
void task()
{
	scanf("%d%d",&n,&nk);
	rep(i,n)cin>>ind[i];
	sort(ind+1,ind+n+1);
	//rep(i,n)cout<<ind[i]<<" ";
	//cout<<endl;
	double tmax=0;
	/*int nz=1<<n;
	for(int iz=0;iz<nz;++iz)
	{
		int tct=0;
		rep(i,n)
		{
			if(iz&1<<i-1)
			{
				++tct;
				meet[i]=true;
			}
			else meet[i]=false;
		}
		if(tct==nk)
		{
			tmax=max(tmax,calc());
		}
	}*/
	double tmax2=0;
	rep2(i,0,nk)
	{
		meet[i]=true;
		rep2(j,i+1,n)meet[j]=false;
		rep2(j,n-(nk-i)+1,n)meet[j]=true;
		/*if(tmax2<calc())
		{
			tmax2=calc();
			for(int i=1;i<=n;++i)cout<<meet[i]<<" ";
			cout<<endl;
		}*/
		tmax2=max(tmax2,calc());
	}
	//assert(tmax==tmax2);
	printf("%.10f\n",tmax2);
	//cout<<tmax<<endl;
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt)
	{
		printf("Case #%d: ",i);
		task();
	}
}
