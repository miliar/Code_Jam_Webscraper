#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <stdlib.h>
#include <math.h>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
 
using namespace std;
 
#define fi first
#define sc second
#define ff first.first
#define fs first.second
#define sf second.first
#define ss second.second
#define pb push_back
#define mp make_pair
#define ll long long
#define dl double
#define ison(a,b) (a&(1<<b))
#define bitcnt __builtin_popcount
#define MOD 1000000007 
#define INF 1000000000
 
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<iii> wadj;

int cnt,n,j;

ll mpow(ll m,ll t)
{
  if(t==0) return 1;
  ll ret=mpow(m,t/2);
  ret=ret*ret;
  if(t%2==1) ret=ret*m;
  return ret;
}

ll check(ll num)
{
  for(ll i=2;i*i<=num;i++)
    if(num%i==0)
      return i;
  return 0;
}

void solve(int s[],int l)
{

  if(cnt>=j)
    return;
  if(l==n-1)
  {
    bool found = false;
    ll ans;
    vector<ll> v;

    for(int i=2;i<=10;i++)
    {
      ll num=0;

      for(int j=n-1;j>=0;j--)
        num += s[j]*mpow(i*1LL,(n-1-j)*1LL);
       ans = check(num);
       
      if(!ans)
        break;
      else
        v.pb(ans);
    }
    if(ans)
    {
      for(int i=0;i<n;i++)
        printf("%d",s[i]);
      for(auto i : v)
        printf(" %lld ",i);
      
      cnt++;
      printf("\n");
    }
    return;

  }
  s[l]=0;
  solve(s,l+1);
  s[l]=1;
  solve(s,l+1);
}
int main(int argc, char const *argv[])
{
//freopen("inp.txt","r",stdin);
//freopen("out.txt","w",stdout);
 int t;
 cin>>t;
 printf("Case #1:\n");
 cin>>n>>j;
 if(n==2)
 return 0;
 int s[50];
 memset(s,0,sizeof(s));
 s[0]=s[n-1]=1;
 solve(s,1); 
    return 0;
}
 