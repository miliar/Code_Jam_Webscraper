#include <bits/stdc++.h>


using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef long double LD;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
#define CLR(a) memset((a), 0 ,sizeof(a))


string s;
bool ary[101],ary2[101];
int main()
{
  int n,cou;
  cin >> n;
  REP(i,n)
  {
    cin >> s;
    cou=0;
    REP(j,s.size())
      ary[j]=s[j]=='+';
    REP(j,s.size()-1)
    {
      if(ary[j]!=ary[j+1])
      {
        cou++;
        REP(k,j+1)
          ary2[k]=ary[k];
        REP(k,j+1)
        {
          ary[k]=!ary2[j+1-k-1];
        }
      }
    }
    if(!ary[0]) cou++;

    printf("Case #%d: %d\n", i+1, cou);
  }
}
