//#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream cin ("B-large.in");
ofstream cout ("B-large.out");
int A[100][100];

string run() {
  int n, m;
  cin >> n >> m;
  for (int i=0; i<n; i++)
    for (int j=0; j<m; j++)
      cin >> A[i][j];
  for (int i=0; i<n; i++)
    for (int j=0; j<m; j++) {
      bool fail = 0;
      for (int k=0; k<n; k++)
        if (A[i][j] < A[k][j]) {
          fail = 1;
          continue;
        }
      if (!fail) continue;
      fail = 0;
      for (int k=0; k<m; k++)
        if (A[i][j] < A[i][k]) {
          fail = 1;
          continue;
        }
      if (fail) return "NO";
    }
  return "YES";
}

int main () {
  int T; cin >> T;
  for (int i=1; i<=T; i++) {
    cout << "Case #" << i << ": " << run() << endl;
  }
  return 0;
}
