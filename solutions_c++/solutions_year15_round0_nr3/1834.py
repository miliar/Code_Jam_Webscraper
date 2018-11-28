#include <iostream> 
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
int table[5][5]={
	{0,0,0,0,0},
	{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1}
};
int nl;
long long nr;
char ts[10002];
int ind[10002];
inline int mul(int ia,int ib)
{
	if((ia>0)^(ib>0))return -table[abs(ia)][abs(ib)];
	return table[abs(ia)][abs(ib)];
}
inline int mul(int ia,int ib,int ic)
{
	return mul(mul(ia,ib),ic);
}
inline int fastmul(int ia,long long ip)
{
	int res=1;
	while(ip)
	{
		if(ip&1)res=mul(res,ia);
		ia=mul(ia,ia);
		ip>>=1;
	}
	return res;
}
void task()
{
	scanf("%d",&nl);
	scanf("%lld",&nr);
	scanf("%s",&ts[1]);
	rep(i,nl)
	{
		ind[i]=ts[i]-'i'+2;
	}
	int nres=1;
	rep(i,nl)
	{
		nres=mul(nres,ind[i]);
	}
	int nrres=fastmul(nres,nr);
	if(nrres!=-1)
	{
		printf("NO\n");
		return;
	}
	int minl=99999999,minr=99999999;
	int tr=min(nr-1,3LL);
	int tarr[4],tcal;
	rep2(i,0,tr)
	{
		tarr[i]=fastmul(nres,i);
	}
	tcal=1;
	rep(i,nl)
	{
		tcal=mul(tcal,ind[i]);
		rep2(k,0,tr)
		{
			if(mul(tarr[k],tcal)==2)minl=min(minl,i+k*nl);
		}
	}
	
	
	tcal=1;
	for(int i=nl;i;--i)
	{
		tcal=mul(ind[i],tcal);
		rep2(k,0,tr)
		{
			if(mul(tcal,tarr[k])==4)minr=min(minr,nl-i+1+k*nl);
		}
	}
	printf(minl+minr<nl*nr?"YES\n":"NO\n");
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
