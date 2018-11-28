// Jakub Radoszewski

//#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
#include<numeric>
#include<cassert>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define INFTY 100000000
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define SIZE(x) ((int)(x).size())

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

ll nwd(ll a,ll b) { return !b?a:nwd(b,a%b); }
inline int CEIL(int a,int b) { return a%b ? a/b+1 : a/b; }
template <class T> inline T sqr(const T&a) { return a*a; }

int los(int m)
{
  return (int)((double)m*(rand()/(RAND_MAX+1.0)));
}

int n;
char tab[10][10];

inline bool sprawdz(int i,VI t,int c)
{
  if (i>=n) return true;
  bool ok=true;
  int ile=0;
//  printf("%d: %d\n",i,t[i]);
  REP(j,n) if (tab[t[i]][j]=='1' && !(c & (1<<j)))
  {
    //printf("%d - %d\n",t[i],j);
    ok=(ok & sprawdz(i+1,t,c | (1<<j)));
    ++ile;
  }
  return (ile>0) && ok;
}

inline bool dobra()
{
  VI t;
  REP(i,n) t.PB(i);
  do
  {
    if (!sprawdz(0,t,0)) return false;
  } while (next_permutation(ALL(t)));
  return true;
}

char t[10][10];

void mymain()
{
  scanf("%d",&n);
  REP(i,n)
  {
    scanf("%s",t[i]);
  }
  int wyn=100;
  REP(mask,(1<<(n*n)))
  {
    int ii=0;
    bool zle=0;
    REP(i,n) if (!zle) REP(j,n)
    {
      if (mask&(1<<ii))
      {
        if (t[i][j]=='1') { zle=1; break; }
        tab[i][j]='1';
      } else
      {
        tab[i][j]=t[i][j];
      }
      ++ii;
    }
    if (zle) continue;
    int b=__builtin_popcountl(mask);
    if (b>wyn) continue;
/*    printf("mask %d\n",mask);
    REP(i,n)
    {
      REP(j,n) putchar(tab[i][j]);
      puts("");
    }*/
    if (dobra()) wyn=b;
  }
  printf("%d\n",wyn);
}

int main()
{
  int ILE;
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    fprintf(stderr,"Case #%d:\n",iii);
    mymain();
  }
  return 0;
}
