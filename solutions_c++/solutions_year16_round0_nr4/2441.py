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

ll mpow(ll m,ll t)
{
  if(t==0) return 1;
  ll ret=mpow(m,t/2);
  ret=ret*ret;
  if(t%2==1) ret=ret*m;
  return ret;
}

int main(int argc, char const *argv[])
{
//freopen("inp.txt","r",stdin);
//freopen("out.txt","w",stdout);
 int t;
 cin>>t;
 for(int j=1;j<=t;j++)
 {
  printf("Case #%d: ",j);
  ll c,k,s;
  cin>>k>>c>>s;
  ll ans =0;
  for(int i=1;i<=k;i++)
  {
    if(!ans)
      printf("1 "),ans++;
    else
      {
        ans = ans + mpow(k,c-1);
        printf("%lld ",ans);
      }
  }
  printf("\n");
 }
 
    return 0;
}
 