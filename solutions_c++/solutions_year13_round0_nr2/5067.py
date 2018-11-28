#include <vector>
#include <string>
#include <iostream>

using namespace std;

#define for0(i,l) for(int i = 0; i < (l); ++i)

bool possible (int n, int m, vector < vector <int> > b, vector < vector <bool> >
    &c) {
  bool row = true;
  bool col = true;

  for0(i, b[n].size()) 
    if (b[n][i] > b[n][m])
      row = false;
  if (row) {
    for0(i, b[n].size()) 
      c[n][i] = true;
  }

  for0(i, b.size()) 
    if (b[i][m] > b[n][m])
      col = false; 
  if (col) {
    for0(i, b.size()) 
      c[i][m] = true;
  }

  return row || col;
}


int main () {
  int T;
  cin >> T;
  for0(t,T) {
    int N, M;
    cin >> N >> M;
    vector < vector <int> > b (N, vector<int> (M, 100));
    for0(n,N)
      for0(m,M)
        cin >> b[n][m];

    string output = "YES";
    for(int h = 1; h <= 100; ++h) {
      vector < vector <bool> > c (N, vector<bool> (M, false));
      for0(n,N) {
        for0(m,M) {
          if (b[n][m] != h)
            continue;
          if (!c[n][m] && !possible(n,m,b,c)) {
            h = 1000; n = N; m = M;
            output = "NO";
          }
        }
      }
    }

    cout << "Case #" << t+1 << ": " << output << endl;
  }
}
