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
int n;

double a[300];
double dp[300][300];

double cnt( vector<double> & p ){
   int k = p.size();

  // REP(i,k) cout << p[i] << ",";
   //cout << endl;

   dp[0][0] = 1.0-p[0];
   dp[0][1] = p[0];

    FOR(i,1,k-1){
      REP(j,i+2){
        if(j == 0) dp[i][j] = dp[i-1][j] * (1.0-p[i]);
        else if(j == i+1) dp[i][j] = dp[i-1][j-1] * p[i];
        else{
          dp[i][j] = dp[i-1][j]  * (1.0 -p[i]) + dp[i-1][j-1]  * p[i];
        }
      }

    }

    return dp[k-1][k/2];


}


int main() {
  // freopen("B.in","r",stdin);
  //  freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
  	freopen("B-small-attempt1.in","r",stdin);freopen("B-small-attempt1.out","w",stdout);
  //	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
	//  freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);

  DRI(cs);
  FOR(ci,1,cs){
    DRII(n,k);
    REP(i,n)scanf("%lf", &a[i] );
    sort(a,a+n);
    vector<double> p;
    /*int nad = 0;
    int pod = 0;
    REP(i,n) if(a[i] = 0.5){ nad++; pod++;}
    else if( a[i] < 0.5) pod++;
    else nad++;*/

    //cout << a[0] << endl;

    double mx = 0.0;
    REP(i,1<<n){
      p.clear();
      REP(j,n){
        if( i & (1<<j) )p.PB(a[j]);
      }
      if(p.size() == k ){
        mx= max(mx, cnt(p) );
      }
    }
    /*
    if(pod < k/2)

    REP(i,k/2){
      p.PB(a[i]);
    }
    FORD(i,n-1, n-k/2) p.PB(a[i]);
    sort(p.begin(),p.end());

    double out = cnt(p);

    /*p.clear();
    REP(i,k)p.PB(a[i]);
    double out2 = cnt(p);

    if (out2 > out) DEB(ci)
    cout << out2 << endl;*/


    printf("Case #%d: %.10lf\n",ci, mx );

  }
  return 0;
}
