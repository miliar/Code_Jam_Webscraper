#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
	
using namespace std;

string grid[101];
int d[300];

int main() {
  int T;

  cin >> T;

	d['^'] = 0;
	d['>'] = 3;
	d['v'] = 1;
	d['<'] = 2;

  for (int t=1;t<=T;t++) {
    int R, C;
    cin >> R >> C;

		for (int i=0;i<R;i++) {
			cin >> grid[i];
		}

		bool impossible = false;
		int count = 0;
		for (int i=0;i<R;i++) for (int j=0;j<C;j++) {
			if (grid[i][j] == '.') continue;
			bool g[4]={};
			for (int k=i-1;k>=0;k--) if (grid[k][j] != '.') {g[0] = true; break;}
			for (int k=i+1;k<R;k++) if (grid[k][j] != '.') {g[1] = true; break;}
			for (int k=j-1;k>=0;k--) if (grid[i][k] != '.') {g[2] = true; break;}
			for (int k=j+1;k<C;k++) if (grid[i][k] != '.') {g[3] = true; break;}
			if (g[d[grid[i][j]]]) {}
			else {
				bool good = false;
				for (int k=0;k<4;k++) if (g[k]) good = true;

				if (!good) impossible = true;
				else count++;
			}
		}
		if (impossible) printf("Case #%d: IMPOSSIBLE\n",t);
		else printf("Case #%d: %d\n",t,count);
  }

}
