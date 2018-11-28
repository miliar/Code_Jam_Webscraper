#include <stdio.h>
#include <iostream>
#include <vector>
#include <bitset>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <math.h>
#include <fstream>
using namespace std;
#define IN(a)          scanf("%d", &a)
#define IN2(a, b)    scanf("%d%d", &a, &b)
#define IN3(a,b, c) scanf("%d%d%d", &a, &b, &c)
#define ENDL              printf("\n")
#define FOR0(n)     for(unsigned int i=0; i<n; i++)
#define FOR1(n)     for(unsigned int i=1; i<=n; i++)
#define FOR(i,a, b)  for(unsigned int i=a; i<b; i++)
#define FORV(a)	  for(int i=0; i<(int)a.size(); i++)
#define FORT(t,a)	  for(t::itr it=a.begin(); it!=a.end(); ++it)
#define mxc(mx, c)	{if((mx)<(c)) {(mx)=(c);}}
#define mnc(mn, c)	{if((mn)>(c)) {(mn)=(c);}}
#define itr			        iterator
#define fi                  first
#define se                second
#define CLR(a)         memset(a, 0, sizeof a)
#define LINF     4611686018427387904LL
#define WHITE  0
#define BLACK  1
#define GRAY    2
#define COMMENT(args...) DEBUG(printf(args); ENDL;)
#define TT DEBUG(printf("\t\t");)
#define DEBUG(X)		X
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
enum { INF = 1000000000, D = 1250 };
int d;
struct comp
{
  bool operator()(const ii& i,const ii& j){
    return (double)i.fi/(double)i.se<(double)j.fi/(double)j.se;
  }
};
int main()
{
  ifstream fin("B-small-attempt1.in");
  ofstream fout("B-small-attempt1.out");
  int TC; fin>>TC; FOR1(TC)
  {
    fin>>d;
    map<ii, int, comp> p;
    FOR0(d)
    {
      int tmp;
      fin>>tmp;
      p[ii(tmp, 1)]++;
    }
    int sol = INF;
    int time = 0;
    while(1)
    {
      map<ii, int>::itr it = p.end();
      --it;
      int num = it->fi.fi;
      int div = it->fi.se;
      int cnt = it->se;
      int nw = (num+div-1)/div+time;
      mnc(sol, nw);
      if(nw<=time+1) break;
      time+=cnt;
      p.erase(it);
      p[ii(num, div+1)]+=cnt;
    }
    fout<<"Case #"<<i<<": "<<sol<<endl;
  }
  return 0;
}












