#include <cstdio>
#include <sstream>
#include <iostream>
#include <memory>
#include <cassert>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int n, m;

bool winning (int A[4][4]) {
  int i,j,k;

  // Row & col check
  fi(4){
    if (A[i][0] == 1 && A[i][1] == 1 && A[i][2] == 1 && A[i][3] == 1) {
      return true;
    }

    if (A[0][i] == 1 && A[1][i] == 1 && A[2][i] == 1 && A[3][i] == 1) {
      return true;
    }
  }

  if (A[0][0] == 1 && A[1][1] == 1 && A[2][2] == 1 && A[3][3] == 1) {
    return true;
  }

  if (A[0][3] == 1 && A[1][2] == 1 && A[2][1] == 1 && A[3][0] == 1) {
    return true;
  }

  return false;
}

int main (int argc, char *argv[]) {

  int i, j, k, t, tt;
  int A[4][4], B[4][4];
  char symbol;
  bool finished;

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> n;

  fi(n) {
    finished = true;
    fj(4) fk(4){
      cin >> symbol;

      // TODO check game ended
      if (finished) {
        if (symbol == '.') {
          finished = false;
        }
      }

      if (symbol == 'X' || symbol == 'T') {
        A[j][k] = 1;
      } else {
        A[j][k] = 0;
      }

      if (symbol == 'O' || symbol == 'T') {
        B[j][k] = 1;
      } else {
        B[j][k] = 0;
      }
    }

    bool a_win = winning(A);
    bool b_win = winning(B);

    cout << "Case #" << i+1 << ": ";

    if (a_win && !b_win)
      {
        cout << "X won" << endl;
      }
    else if (b_win && !a_win )
      {
        cout << "O won" << endl;
      }
    else if(finished)
      {
        cout << "Draw" << endl;
      }
    else
      {
        cout << "Game has not completed" << endl;
      }
  }

  return 0;
}
