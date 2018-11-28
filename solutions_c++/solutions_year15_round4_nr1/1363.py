#include <bits/stdc++.h>

using namespace std;

#define upto(i,n) for (int i = 0; i<n; ++i)

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int MAX = 1000;
const ll MOD = 1000000007;



char A[102][102];


void solve() {
  int r,c;

  cin >> r >> c;

  upto(i,r) upto(j,c) cin >> A[i][j];

  int sum = 0;
  int up, down, left, right;

  upto(i,r) upto( j,c) {
    up = 0;
    down = 0;
    left = 0; 
    right = 0;
    if ( A[i][j] != '.') {
      for(int k = j+1; k<c; k++)  if ( A[i][k] != '.' ) { right = 1; break;}
      for(int k = j-1; k>=0; k--) if ( A[i][k] != '.' ) { left  = 1; break;}
      for(int k = i+1; k<r; k++)  if ( A[k][j] != '.' ) { down  = 1; break;}
      for(int k = i-1; k>=0; k--) if ( A[k][j] != '.' ) { up    = 1; break;}
      if ( up + down + left + right == 0 ) {
        sum = -1;
        goto END;
      }
      switch ( A[i][j] ) {
        case '<': if ( !left) sum++;
                  break;
        case '>': if ( !right ) sum++;
                  break;
        case 'v': if ( !down) sum++;
                  break;
        case '^': if ( !up) sum++;
                  break;

        default: break;
      }
    }
  }

END:
  if ( sum == -1 )
    cout << "IMPOSSIBLE" << endl;
  else
    cout << sum << endl;
}

int main() {
  int t;

  cin >> t;
  for ( int tc = 1; tc<=t; ++tc) {
    cout << "Case #" << tc<< ": ";
    solve();
  }
  return 0;
}

