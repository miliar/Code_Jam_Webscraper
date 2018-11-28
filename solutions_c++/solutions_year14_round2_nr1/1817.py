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

#define MAX 105

int T, N;
string pole[MAX];
pair<char, vector<int> > r[MAX];

int solve() {
  int max_pointer = -1;
  FOR (i, 0, N-1) {
    char last = '8';
    int pointer = -1;
    FOR (j, 0, SIZE(pole[i])-1) {
      if (pole[i][j] != last) {
        pointer++;
        if (i == 0) {
          vector<int> v;
          v.PB(1);
          r[pointer] = MP(pole[i][j], v);
        } else {
          if (pointer > max_pointer || pole[i][j] != r[pointer].fi) return -1;

          r[pointer].se.PB(1);
        }
        

      } else {
        r[pointer].se[i]++;
      }

      last = pole[i][j];
    }

    if (i == 0) {
      max_pointer = pointer;
    } else {
      if (max_pointer != pointer) return -1;
    }
  }

  /*
  FOR (i, 0, max_pointer) {
    cout << "char " << r[i].fi << endl;
    FOR (j, 0, N-1) {
      cout << r[i].se[j] << endl;
    }
    cout << "---" << endl;
  }
  */
  

  int res = 0;
  FOR (i, 0, max_pointer) {
    int mmm = 0;
    FOR (j, 0, N-1) {
      mmm += r[i].se[j];
    }
    int avg = mmm / N;

    if (mmm % N != 0) {
      int ax = 0;
      FOR (j, 0, N-1)
        ax += abs(r[i].se[j] - avg);

      int bx = 0;
      FOR (j, 0, N-1)
        bx += abs(r[i].se[j] - (avg+1));

      res += min(ax, bx);
    } else {

      FOR (j, 0, N-1) {
        res += abs(r[i].se[j] - avg);
      }
    }
  }

  return res;
}

int main() {
  scanf("%d", &T);
  FOR (caser, 1, T) {
    scanf("%d", &N);
    FOR (i, 0, N-1) {
      cin >> pole[i];
    }

    int res = solve();
    if (res == -1) {
      printf("Case #%d: Fegla Won\n", caser);
    } else {
      printf("Case #%d: %d\n", caser, res);
    }
  }

  return 0;
}
