#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<unordered_set>
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
#define PLD pair<LD,LD>
using namespace std;
int n,m,a,b,c,d;
char ch;
vector<string> in[103];
void solve()
  {
  scanf("%d ",&n);
  unordered_set<string> zero,jeden;
  
  FOR(i,0,n-1)
    {
    scanf(" ");
    in[i].clear();
    string s,x;
    getline(cin,s);
//    cerr<<s<<endl;
    REP(j,s.size())
      {
      if(s[j]==' ')
        {
        in[i].PB(x);
        x="";
        }
      else
        {
        x+=s[j];
        }
      }
    in[i].PB(x);
    }
   int startres=0;
   REP(u,in[0].size())
      {
      zero.insert(in[0][u]);
      }
   REP(u,in[1].size())
      {
      jeden.insert(in[1][u]);
      }
   for(auto it:zero)
      {
      if(jeden.count(it))startres++;
      }
//  cerr<<"startres "<<startres<<endl; 
  int res=1e9;
  //1-angol 0-francuski
  unordered_set<string> S[2];
  S[0]=zero;
  S[1]=jeden;
  REP(i,1<<n)
    {
    if((i&1)&&!(i&2));
    else continue;
    int ter=startres;
    REP(j,n)
      {
      if(j<2)continue;
      bool dzie=((i&(1<<j))>0);
      REP(u,in[j].size())
        {
        if(S[dzie].count(in[j][u])==0&&S[dzie^1].count(in[j][u]))
          {
          ter++;
          }
        S[dzie].insert(in[j][u]);
        }

      }
    mini(res,ter);
    
    FOR(j,2,n-1)
      {
      REP(u,in[j].size())
        {
        string s=in[j][u];
        if(jeden.count(s)==0&&S[1].count(s))S[1].erase(s);
        if(zero.count(s)==0&&S[0].count(s))S[0].erase(s);
        }
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
