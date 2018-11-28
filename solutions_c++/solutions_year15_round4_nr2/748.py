#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
#define MP make_pair
#define PB push_back
#define ff first
#define ss second
#define TR(it,c) for( typeof(c.begin()) it = c.begin(); it != c.end(); ++it )
#define TRR(it,c) for( typeof(c.rbegin()) it = c.rbegin(); it != c.rend(); ++it
#define REP(i,a) for (int i = 0; i < (a); i++)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

#define DRI(a) int a; scanf("%d", &a);
#define DRII(a, b) int a, b; scanf("%d %d", &a, &b);
#define DRIII(a, b, c) int a, b, c; scanf("%d %d %d", &a, &b, &c);
#define RI(a) scanf("%d", &a);
#define RII(a, b) scanf("%d %d", &a, &b);
#define RIII(a, b, c) scanf("%d %d %d", &a, &b, &c);
#define MM(arr, num) memset((arr), (num), sizeof((arr)))
#define DEB(x) cerr << ">>> " << (#x) << " -> " << (x) << endl;
#define DEBA(x,n) cerr << (#x) << " "; deba((x),(n));
void deba(int * a, int n){ cerr << "| "; REP(i,n) cerr << a[i] << " "; cerr << "|" << endl;}


inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<30;
typedef long long ll;
typedef unsigned long long ull;
/*******************************************************/

pair< double, double> r[123];



int main() {
//    freopen("B.in","r",stdin);
  freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
//	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);

  DRI(cs);
  FOR(ci,1,cs){
    int n;
    double V,C;
    cin >> n >> V >> C;
    REP(i,n) cin >> r[i].ss >> r[i].ff ;

    sort(r, r+n);

    if (n==1){
        if ( EQ(r[0].ff,C) ){
          printf("Case #%d: %.8lf\n",ci, V / r[0].ss );
        }
        else printf("Case #%d: IMPOSSIBLE\n",ci);
    }
    else if(n == 2){

        double temp = (r[0].ss*r[0].ff+r[1].ss*r[1].ff)/(r[0].ss+r[1].ss);

        if ( EQ(r[0].ff, C) && EQ(r[1].ff,C) )printf("Case #%d: %.8lf\n",ci, V / (r[0].ss + r[1].ss) );
        else if ( EQ(r[0].ff, C) )printf("Case #%d: %.8lf\n",ci, V / (r[0].ss ) );
        else if ( EQ(r[1].ff,C) )printf("Case #%d: %.8lf\n",ci, V / (r[1].ss) );
        else if ( r[0].ff < C && r[1].ff < C )printf("Case #%d: IMPOSSIBLE\n",ci);
        else if ( r[0].ff > C && r[1].ff > C )printf("Case #%d: IMPOSSIBLE\n",ci);
        else if (temp > C){

           double x =  ( ( C * r[0].ss ) - ( r[0].ff * r[0].ss) ) /  (r[1].ff - C) ;
           x += r[0].ss;
           printf("Case #%d: %.8lf\n",ci, V / x );
        }
        else{
           DEB(1)
           double x = ( ( C * r[1].ss ) - ( r[1].ff * r[1].ss) ) /  (r[0].ff - C) ; ;
           x+= r[1].ss;
           printf("Case #%d: %.8lf\n",ci, V / x );

        }

    }




  }
  return 0;
}
