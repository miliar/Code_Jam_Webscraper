//--BY--©--WA-
#include<iostream> //cout, cin, getline

#include<algorithm> //find, reaplce, swap, sort, lower_bound, uper_bound, binnary_search...
#include<vector> //push_back, size, resize, 
#include<string>
#include<queue> //empty, front, back, push
#include<stack> //push, top, empty
#include<map>
#include<set>
#include<list> //spajazny zoznam .. vsetko v O(1)

#include<stdio.h> //printf, scanf, getchar, putchar
#include<math.h> //cos, sin, exp, pow, sqrt,  flnoor, cell
#include<stdlib.h> //atio, atl, strtod, strtol, atof, abs, 
#include<ctype.h> //isalnum, isalpha, isdigit, islower, isupper, toupper, tolower, 
#include<string.h> //strcm, strstr, strlen,

using namespace std;

#define FOREACH(obj,it) for(__typeof(obj.begin()) it = (obj).begin(); it != (obj).end(); (it)++)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i,a,b) for(int i=a; i>=b; i--)
#define REP(i,a,b) for(int i=a; i<b; i++)
#define DEBUG(V,S) FOR(i,0,S-1){cout << i << ". " << V[i] << endl;}

#define PB push_back
#define PII pair<int,int>
#define PLL pair<ll,ll>
#define MP make_pair
#define fi first
#define se second

#define SIZE(s) (int) (s).size()

#define INF 987654321
#define EPS 1e-9
#define ld long double // %Lf, double %lf
#define ll long long   // %llf

//--------------------------------------------------------------------------------------

PII solve() {
  int N;
  double pA[1012], pB[1012];

  scanf("%d", &N);
  FOR (i, 0, N-1) scanf("%lf", &(pA[i]));
  FOR (i, 0, N-1) scanf("%lf", &(pB[i]));

  sort(pA, pA+N);
  sort(pB, pB+N);

  int dw = 0;

  int point = 0;
  FOR (i, 0, N-1) {
    if (pA[i] > pB[point]) {
      dw++;
      point++;
    }
  }


  
  int w = 0;
  bool usedB[1012];
  FOR (i, 0, N-1) usedB[i] = false;
  
  FOR (i, 0, N-1) {
    int ma = -1;
    FOR (j, 0, N-1) {
      if (!usedB[j] && pB[j] > pA[i] && (ma == -1 || pB[j] < pB[ma])) {
        ma = j;
      }
    }
    if (ma == -1) {
      w++;
      FOR (j, 0, N-1) {
        if (!usedB[j]) {
          usedB[j] = true;
          break;
        }
      }
    } else {
      usedB[ma] = true;
    }
  }

  return MP(dw, w);
}


int main() {
  int Q;
  scanf("%d", &Q);
  FOR (caser, 1, Q) {
    printf("Case #%d: ", caser);

    PII res = solve();
    printf("%d %d\n", res.fi, res.se);
  }

	return 0;
}
