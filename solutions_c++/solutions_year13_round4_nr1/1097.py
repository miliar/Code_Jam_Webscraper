#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
using namespace std;
#define p(x) cout<<#x<<":"<<x<<"\n"
#define mod 1000002013
#define f first
#define s second
#define mp make_pair
#define ll long long

ll cs,c,n,m,i,z,s,e,a,j;
bool f;
pair <ll,ll> A[10001];

ll g(ll s,ll e)
{
  ll d=e-s;
  
  return d*(n+1)-d*(d+1)/2;
}
int main()
{
  scanf("%lld",&cs);
  for(c=1;c<=cs;c++)
  {
    cerr<<c<<"\n";
    scanf("%lld%lld",&n,&m);
	for(i=z=0;i<m;i++)
	{
	  scanf("%lld%lld%lld",&s,&e,&a);
	  for(j=0;j<a;j++)
	    A[z++]=mp(s,e);
	}
	sort(A,A+z);
	/*for(i=0;i<<;i++)
	  if(!Q.empty() && Q.top().f<A[i].f && Q.top().s<A[i].s)
	  {
	    s=Q.top().f;
	    e=Q.top().s;
		Q.push(mp(s,E[i]));
		Q.push(mp(S[i],e));
	  }*/
	s=0;
	for(i=0;i<z;i++)
	{
	  s=(s+g(A[i].f,A[i].s))%mod;
	}
	f=1;
	while(f)
	  for(i=f=0;i<z;i++)
	    for(j=i+1;j<z;j++)
		{
		  if(A[i].s>=A[j].f && g(A[i].f,A[j].s)+g(A[j].f,A[i].s)<g(A[i].f,A[i].s)+g(A[j].f,A[j].s))
		  {
		    swap(A[i].s,A[j].s);
		    f=1;
		  }
		}
	e=0;
	for(i=0;i<z;i++)
	  e=(e+g(A[i].f,A[i].s))%mod;
    printf("Case #%lld: %lld\n",c,(s-e+mod)%mod);
  }
  return 0;
}
