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

string t[14][3];

void gen()
{
  t[0][0]=string("P");
  t[0][1]=string("R");
  t[0][2]=string("S");
  FOR(i,1,12) REP(j,3) t[i][j]=string("Z");
  FOR(i,0,11)
  {
    REP(j,3) REP(k,3) if (j!=k)
    {
      int a=j,b=k;
      if (a>b) swap(a,b);
      int c=-1;
      if (a==0 && b==1) c=0;
      if (a==1 && b==2) c=1;
      if (a==0 && b==2) c=2;
      t[i+1][c]=min(t[i+1][c],t[i][j]+t[i][k]);
    }
  }
}

void policz(string s,int &a,int &b,int &c)
{
  a=b=c=0;
  REP(i,SIZE(s)) if (s[i]=='P') ++a; else if (s[i]=='R') ++b; else ++c;
}

void mymain()
{
  int N,p,r,s;
  scanf("%d%d%d%d",&N,&r,&p,&s);
  string w="Z";
  REP(i,3)
  {
    assert(!t[N][i].empty());
    int a,b,c;
    policz(t[N][i],a,b,c);
    if (a==p && b==r && c==s)
    {
      w=min(w,t[N][i]);
    }
  }
  if (w!=string("Z")) puts(w.c_str()); else puts("IMPOSSIBLE");
}

int main()
{
  gen();
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
