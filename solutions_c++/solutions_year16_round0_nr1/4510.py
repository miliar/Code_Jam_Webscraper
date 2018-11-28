#include <bits/stdc++.h>


using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef long double LD;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define CLR(a) memset((a), 0 ,sizeof(a))


bool dig[10];
void check(LL n)
{
  if(n==0) return;
  dig[n%10]=true;
  check(n/10);
}
int main()
{
  int t;
  bool flag;
  cin>>t;
  LL n;
  REP(i,t)
  {
    CLR(dig);
    cin>>n;
    for(int j=1;j<1000000;j++)
    {
      check(n*j);
      flag=true;
      REP(k,10)
        if(!dig[k])
          flag=false;
      if(flag)
      {
        printf("Case #%d: %lld\n",i+1, n*j);
        break;
      }
      else if(j==1000000-1)
        printf("Case #%d: INSOMNIA\n",i+1);
    }
  }
}
