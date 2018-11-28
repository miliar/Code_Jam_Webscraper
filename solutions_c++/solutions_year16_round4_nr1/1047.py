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


string build( string c, int i, int n ){

    //cout << c << endl;

    if( i == n+1) return c;
    string out, out2;
    if( c == "P"){ out= build( "P" , i+1, n); out2 = build( "R", i+1, n); }
    if( c == "R"){ out= build( "R" , i+1, n); out2 = build( "S", i+1, n); }
    if( c == "S"){ out= build( "P" , i+1, n); out2 = build( "S", i+1, n); }
    return ( out < out2 ) ? out+out2 : out2 + out;
}

int main() {
  // freopen("A.in","r",stdin);
  //  freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
  //	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
  //	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	  freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

  DRI(cs);
  FOR(ci,1,cs){
    DRII(N,R);
    DRII(P,S);

    printf("Case #%d: ",ci);

    if(N == 1){
      if(P==2 || R == 2 || S==2){ printf("IMPOSSIBLE");}
      else{ if(P) printf("P");
          if(R) printf("R");
          if(S) printf("S");
      }
    }
    else{
      string out; int p,r,s;
      vector<string> vec;
      p =r=s=0;
      out = build("P",1, N);
      REP(i,out.size()) if( out[i] == 'P')p++;
      REP(i,out.size()) if( out[i] == 'R')r++;
      REP(i,out.size()) if( out[i] == 'S')s++;
      if(p == P && r == R && s == S){ vec.PB(out);}

      p =r=s=0;
      out = build("R",1, N);
      REP(i,out.size()) if( out[i] == 'P')p++;
      REP(i,out.size()) if( out[i] == 'R')r++;
      REP(i,out.size()) if( out[i] == 'S')s++;
      if(p == P && r == R && s == S){ vec.PB(out);}

      p =r=s=0;
      out = build("S",1, N);
      REP(i,out.size()) if( out[i] == 'P')p++;
      REP(i,out.size()) if( out[i] == 'R')r++;
      REP(i,out.size()) if( out[i] == 'S')s++;
      if(p == P && r == R && s == S){ vec.PB(out);}
      if(vec.size() == 0) printf("IMPOSSIBLE");
      else{
        sort(vec.begin(), vec.end());
        cout << vec[0];
      }
    }
    printf("\n");

  }
  return 0;
}
