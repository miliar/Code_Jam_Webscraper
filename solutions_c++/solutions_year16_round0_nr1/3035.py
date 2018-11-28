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

bool mark[10];

int main(int argc, char const *argv[])
{
//freopen("inp.txt","r",stdin);
 //freopen("out.txt","w",stdout);

  int t;
  cin>>t;
  for(int ts=1;ts<=t;ts++)
  {
    ll n;
    cin>>n;
    memset(mark,0,sizeof(mark));
    ll ans = 0;
    for(int i=1;i<100000;i++)
    {
      ll a = n*i;
    
      while(a)
      {
        int v  = a%10;
        mark[v]=1;
        a/=10;
      }
      bool found = true;

      for(int j=0;j<10;j++)
        if(!mark[j])
          {
          	found=false;
          	break;
          }
        if(found)
        {
        	ans=n*i;
        	break;
        }
    }
    if(!ans)
      printf("Case #%d: INSOMNIA\n",ts);
    else
      printf("Case #%d: %lld\n",ts,ans);

  }
 
 

 
    return 0;
}
