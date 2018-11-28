#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>

#define mp make_pair
#define pb push_back

#define REP(i,n) for(int i=0; i < (n); ++i)

using namespace std;


void solve()
{
	bool success = true;
	int n,m;
	int mmap[150][150];
	bool c[2][150][150] = {0,};

	cin >> n >> m;
	REP(i,n) {
		REP(j,m) {
			cin >> mmap[i][j];
		}
	}

	for(int i = 0; i < n; ++i) {
		int maxrow = -1;
		
		for(int j = 0; j < m; ++j) {
			maxrow = max(maxrow, mmap[i][j]);
		}

		for(int j = 0; j < m; ++j) {
			if(mmap[i][j] < maxrow) c[0][i][j] = true;
		}	
	}

	for(int i = 0; i < m; ++i) {
		int maxrow = -1;
		
		for(int j = 0; j < n; ++j) {
			maxrow = max(maxrow, mmap[j][i]);
		}

		for(int j = 0; j < n; ++j) {
			if(mmap[j][i] < maxrow) c[1][j][i] = true;
		}	
	}


	REP(i, n) {
		REP(j, m) {
			if (c[0][i][j] && c[1][i][j]) {
				cout << "NO" << endl;
				return;
			}
		}
	}
	cout << "YES" << endl;
}

int main(int argc, char *argv[])
{
  int t;
  cin >> t;
  for(int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }

  return 0;
}

