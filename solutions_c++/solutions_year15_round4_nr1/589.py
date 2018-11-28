#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {
    int R,C;
    cin >> R >> C;
    int answer = R*C+1;
    vector<string> G(R);
    for (int i=0; i<R; i++)
      cin >> G[i];
    int flips = 0;
    bool impossible = false;
    for (int i=0; i<R; i++)
      for (int j=0; j<C; j++)
	if (G[i][j] != '.') {
	  flips ++;
	  bool solo = true;
	  for (int k=i+1; k <R; k++) if (G[k][j] != '.') { solo = false; if (G[i][j] == 'v') flips--; break; }
	  for (int k=i-1; k>=0; k--) if (G[k][j] != '.') { solo = false; if (G[i][j] == '^') flips--; break; }
	  for (int k=j+1; k <C; k++) if (G[i][k] != '.') { solo = false; if (G[i][j] == '>') flips--; break; }
	  for (int k=j-1; k>=0; k--) if (G[i][k] != '.') { solo = false; if (G[i][j] == '<') flips--; break; }
	  if (solo) impossible = true;
	};

    cout << "Case #" << t << ": ";
    if (impossible) cout << "IMPOSSIBLE" << endl;
    else cout << flips << endl;
  };
  return 0;
};
