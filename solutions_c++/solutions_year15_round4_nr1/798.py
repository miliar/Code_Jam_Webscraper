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

char s[123][123]; int H,W;

bool u(int i, int j){
  i--;
  int ok = 0;
  while(i>=0){
    if (s[i][j]!= '.') return true;
    i--;
  }
  return false;

}
bool d(int i, int j){
  i++;
  int ok = 0;
  while(i<H){
    if (s[i][j]!= '.') return true;
    i++;
  }
  return false;

}
bool l(int i, int j){
  j--;
  int ok = 0;
  while(j>=0){
    if (s[i][j]!= '.') return true;
    j--;
  }
  return false;

}
bool r(int i, int j){
  j++;
  int ok = 0;
  while(j<W){
    if (s[i][j]!= '.') return true;
    j++;
  }
  return false;

}

int main() {

   // freopen("A.in","r",stdin);
//  freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

  DRI(cs);
  FOR(ci,1,cs){
    RII(H,W);
    REP(i,H)scanf("%s",s[i]);
    int key = 0;

   int im = 0;
   int num = 0;

    REP(i,H){

      REP(j,W){
        if (s[i][j] != '.'){
          if (s[i][j] == '^'){
              if ( !u(i,j) ){
                num++;
                if ( !d(i,j) && !r(i,j) && !l(i,j) )im= 1;
              }
          }
           if (s[i][j] == 'v'){
              if ( !d(i,j) ){
                num++;
                if ( !u(i,j) && !r(i,j) && !l(i,j) )im= 1;
              }
          }
           if (s[i][j] == '>'){
              if ( !r(i,j) ){
                num++;
                if ( !d(i,j) && !u(i,j) && !l(i,j) )im= 1;
              }
          }
           if (s[i][j] == '<'){
              if ( !l(i,j) ){
                num++;
                if ( !d(i,j) && !r(i,j) && !u(i,j) )im= 1;
              }
          }

        }
      }

    }

    if (im )printf("Case #%d: IMPOSSIBLE\n",ci);
    else printf("Case #%d: %d\n",ci,num);
  }
  return 0;
}
