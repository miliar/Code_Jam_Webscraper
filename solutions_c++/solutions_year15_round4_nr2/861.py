#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
#include <queue>
#include <ctime>
#include <cmath>

using namespace std;

#define forn(I,N) for (int I=0; I<N; I++)
#define fornd(I,N) for (int I=N-1; I>=0; I--)
#define forab(I,A,B) for (int I=A; I<=B; I++)
#define forabd(I,A,B) for (int I=B; I>=A; I--)
#define FOREACH(I,A) for (__typeof__(A)::iterator I=A.begin(); I<A.end(); I++)
#define pb push_back
#define mp make_pair

typedef long long int ll;

int main() {
  int T;
  cin >> T;

  cout << fixed << setprecision(9);
  forn(i, T) {
    int N;
    double V, X;
    cin >> N >> V >> X;

    vector<double> R(N), C(N);
    forn(j, N) {
      cin >> R[j] >> C[j];
    }

    bool possible = true;
    double t;
    if(N == 1) {
      if(C[0] != X) {
        possible = false;
      }
      else {
        t = V / R[0];
      }
    }
    else if (N == 2) {
      if((X < C[0] && X < C[1]) || (X > C[0] && X > C[1])) {
        possible = false;
      }
      else {
        if(C[0] == C[1]) {
          t = V / (R[0] + R[1]);
        }
        else {
          double t1 = (V * X - V * C[1]) / (C[0] - C[1]) / R[0];
          double t2 = (V * X - V * C[0]) / (C[1] - C[0]) / R[1];
          t = max(t1, t2);
        }
      }
    }

    cout << "Case #" << i + 1 << ": ";
    if(possible) {
      cout << t << endl;
    }
    else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
