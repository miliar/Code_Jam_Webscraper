#include <cstring>
#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <vector>
#include <list>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cmath>
using namespace std;
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define ll long long
#define ff first
#define ss second
#define inf  1e9
#define eps  1e-10
#define infll 1e18
#define pr(x) printf("%lld\n",x)
#define sc(x) scanf("%lld",&x)
#define fr(i,a,n) for(i=a;i<n;i++)
#define fd(i,a,n) for(i=n;i>a;i--)
#define fiv(v) for(i=0;i<v.size();i++)
#define clr(a) memset(a,0,sizeof(a))
#define fill(a,v) memset(a,v,sizeof(a))
#define all(a) a.begin(),a.end()
#define iter(c,it) for(typeof((c).begin()) it= (c).begin(); it != (c).end(); it++)
vector<int>v,v1;

int main()
{
    ll i,n,j,k,l,m,t;
    double c,f,x;
    #ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    sc(t);
    for(ll u=1;u<=t;u++)
    {
      scanf("%lf%lf%lf",&c,&f,&x);
      double min_time=x/2;
      double total=c/2;
      double prev=1.0*inf,curr=1.0*inf;
      for(i=1;prev-min_time>eps;i++)
      {
          prev=min_time;
          curr=total+x/(2+f*i);
          total+=c/(2+f*i);
          if(curr<min_time)
            min_time=curr;
      }
      printf("Case #%lld: %0.7lf\n",u,min_time);
    }
    return 0;
}

