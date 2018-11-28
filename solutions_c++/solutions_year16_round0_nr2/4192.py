#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<set>
#define PII pair<int,int>
#define f first
#define s second
#define VI vector<int>
#define LL long long
#define MP make_pair
#define LD long double
#define PB push_back
#define ALL(V) V.begin(),V.end()
#define abs(x) max((x),-(x))
#define PDD pair<LD,LD> 
#define VPII vector< PII > 
#define siz(V) ((int)V.size())
#define FOR(x, b, e)  for(int x=b;x<=(e);x++)
#define FORD(x, b, e) for(int x=b;x>=(e);x--)
#define REP(x, n)     for(int x=0;x<(n);x++)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
using namespace std;
int n,a,b;
bool in[1003];
void solve()
  {
  string s;
  cin>>s;
  int n = 1;
  in[n]=(s[0]=='+');
  REP(i,s.size())
    {
    if(i==0)continue;
    if(s[i]==s[i-1])continue;
    in[++n]=(s[i]=='+');
    }
  int jaki = 1;
  int res = 0;
  FORD(i,n,1)
    {
    if(jaki == in[i])continue;
    else if(i == 1 && jaki !=in[i]){res++;continue;}
    else
      {
      res+=2;
      jaki^=1;
      FOR(j,1,i-1)in[j]^=1;
//      reverse(in+1, in+i);
      }
    }
  printf("%d\n",res);
  }
main()
{
int z;
scanf("%d",&z);
FOR(iii,1,z)
  {
  printf("Case #%d: ",iii);
  solve();
  }
}
