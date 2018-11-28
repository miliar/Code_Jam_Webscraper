#include<algorithm>
#include<bitset>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define dprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &rout, pair<T1, T2> pair) { return rout << "(" << pair.X << ", " << pair.Y << ")";}

const int N = 100;
int r, c;
string s[N];

bool drops(int x, int y) {
  int dx = 0, dy = 0;
  switch (s[x][y]) {
    case '.':
      return false;
    case '<':
      dy = -1;
      break;
    case '>':
      dy = 1;
      break;
    case 'v':
      dx = 1;
      break;
    case '^':
      dx = -1;
      break;
    default:
      printf("WRONG: %c\n", s[x][y]);
      exit(1);
  }

  do {
    x += dx;
    y += dy;

    if (x < 0 || x >= r) {
      return true;
    }
    if (y < 0 || y >= c) {
      return true;
    }
  } while (s[x][y] == '.');
  return false;
}

string possible("<>^v");

void solve(int t) {
  printf("Case #%d: ", t+1);
  
  cin >> r >> c;
  for (int i=0; i<r; ++i) {
    cin >> s[i];
  }

  int result = 0;
  for (int i=0; i<r; ++i) {
    for (int j=0; j<c; ++j) {
      if (drops(i,j)) {

//        printif("Drops %d %d\n", i, j);

        bool ok = false;
        for (int k=0; k<4; ++k) {
          s[i][j] = possible[k];
          if (!drops(i,j)) {
            ok = true;
          }
        }
        if (!ok) {
          printf("IMPOSSIBLE\n");
          return;
        }
        ++result;
      }
    }
  }
  printf("%d\n", result);
}

int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);

    int t; cin >> t;
    for (int i=0; i<t; ++i) {
      solve(i);
    }
    return 0;
}
