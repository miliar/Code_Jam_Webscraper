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

#define INF 987654321443
#define EPS 1e-9
#define ld long double // %Lf, double %lf
#define ll long long   // %llf

//--------------------------------------------------------------------------------------

double solve() {
  double C, F, X;
  scanf("%lf %lf %lf", &C, &F, &X);

  double last_res = INFINITY;
  double cum_F = 0;
  int farms = 0;

  while (true) {
    if (farms > 0) {
      cum_F += (C / (2.0 + (farms-1)*F));
    }

    double r = cum_F + (X / (2.0 + farms*F));
    if (r > last_res) return last_res;
    last_res = r;

    farms += 1;
  }
}

int main() {
  int Q;
  scanf("%d", &Q);
  FOR (caser, 1, Q) {
    printf("Case #%d: %.7lf\n", caser, solve());
  }

	return 0;
}
