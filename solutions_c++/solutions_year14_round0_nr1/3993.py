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

vector<int> solve() {
  int r;
  scanf("%d", &r);

  int pos[4], trash;
  FOR (i, 0, 3) {
    FOR (j, 0, 3) {
      if (r-1 == i)
        scanf("%d", &(pos[j]));
      else
        scanf("%d", &trash);
    }
  }

  vector<int> res;
  int t;

  scanf("%d", &r);
  FOR (i, 0, 3) {
    FOR (j, 0, 3) {
      if (r-1 == i) {
        scanf("%d", &t);
        FOR (k, 0, 3) {
          if (pos[k] == t) {
            res.PB(t);
          }
        }
      }
      else
        scanf("%d", &trash);
    }
  }

  return res;
}

int main() {

  int Q;
  scanf("%d", &Q);
  FOR(caser, 1, Q) {
    vector<int> res = solve();
    printf("Case #%d: ", caser);
    if (SIZE(res) == 0) {
      puts("Volunteer cheated!");
    } else if (SIZE(res) == 1) {
      printf("%d\n", res[0]);
    } else {
      puts("Bad magician!");
    }
  } 

	return 0;
}
