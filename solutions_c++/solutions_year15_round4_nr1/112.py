#include <bits/stdc++.h>
using namespace std;
int main (){
  int Z;
  cin >> Z;
  for (int z = 1; z <= Z; ++z) {
    int n, m;
    cin >> n >> m;
    vector<string> board(n);
    for (int i=0;i<n;++i) cin >> board[i];
    int count = 0;
    bool ok = true;
    for (int i=0; i<n; ++i)
      for (int j=0; j<m; ++j) {
        if (board[i][j] == '.') continue;
        bool possible = false;
        for (int k = 0; k < n; ++k)
          if (k!=i && board[k][j] != '.') possible=true;
        for (int k = 0; k < m; ++k)
          if (k!=j && board[i][k] != '.') possible=true;
        if (!possible) 
          ok = false;
        int di = 0, dj = 0;
        if (board[i][j]=='^') di=-1;
        else if (board[i][j]=='v') di=1;
        else if (board[i][j]=='<') dj=-1;
        else if (board[i][j]=='>') dj=1;
        else assert(false);
        bool has_to_ch = true;
        int ii=i, jj=j;
        while (true) {
          ii += di;
          jj += dj;
          if (ii<0 || jj <0 || ii >=n || jj>=m) break;
          if (board[ii][jj] != '.')
            has_to_ch = false;
        }
        if (has_to_ch) ++count;
      }
    if (!ok)
      cout << "Case #" << z << ": " << "IMPOSSIBLE" << endl;
    else
      cout << "Case #" << z << ": " << count << endl;
  }
}
