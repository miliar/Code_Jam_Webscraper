#ifndef INCLUDES

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <time.h>
#include <unistd.h>
#include <utility>
#include <vector>
using namespace std;

#endif

#ifndef MACROS

#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define SZ(c) ((int)(c).size())
#define CLR(c,v) memset(c, v, sizeof(c))
#define REP(i,e) for(int i = 0; i < (signed)(e); ++i)
#define REPS(i,c) for(int i = 0; i < (int) (c).size(); ++i)
#define FORU(i,b,e) for(__typeof(b) i = (b); i != (e); ++i)
#define FORD(i,b,e) for(__typeof(b) i = (b); i != (e); --i)
#define FORC(i,c) FORU(i,c.begin(),c.end())
typedef vector<int> vi; typedef long long Int;
typedef pair<int,int> pii;

#endif

vector<int> P;
int T, D, pencks, best;
int MR[10] = {-1,0,0,0,1,1,9,9,9,9};

int manage(int minutes, int atCakes, vector<int> pencakes) {
    if (minutes >= best) return 999;
    // cout << pencakes << endl;
    //if (minutes <= 2) { cout << minutes << "| "; REP(i,10) { cout << pencakes[i] << " " ; } cout << endl; }
    for(int i = atCakes; i > 0; --i) {
       if (pencakes[i] > 0) {
           best = min(best, minutes + i);
           if (pencakes[i] > MR[i]) {
                minutes += i;
                return minutes;
           } else {             
               pencakes[i] -= 1;
               int minm = 999;
               for(int j = 1; j <= i/2; ++j) {                   
                   vector<int> vb = pencakes;
                   vb[j] += 1; vb[i-j] += 1;
                   //cout << "INN: " << j << "/" << i-j << " min = " << minutes+1 << endl;
                   minm = min(minm, manage(minutes + 1, atCakes, vb));
                   best = min(best, minm);
                   //if (minutes <= 2) { cout << "OUT: " << j << "/" << i-j << " = " << minm << endl; }
               }
               return minm;
           }           
       }
    }    
}

int main(int argc, char *argv[]) {
  cerr.precision(15);
  cout.precision(15);

  scanf("%d\n",&T);
  REP(testcase,T) {
    best = -1;
    
    scanf("%d\n",&D);
    P.clear();
    REP(i,10) { P.push_back(0); }
    REP(i,D) {
      scanf("%d",&pencks);
      //cout << pencks << " ";
      P[pencks] += 1;
      best = max(best, pencks);
    } //cout << endl;

    printf("Case #%d: %d",testcase+1,min(best, manage(0, 9, P)));
    printf("\n");
  }

  return 0;
}