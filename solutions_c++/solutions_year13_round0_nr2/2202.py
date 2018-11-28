#include <iostream>
#include <cstdio>

using namespace std;

#define N 100

int lawn[N][N];
int maxr[N];
int maxc[N];

bool processOne(int n, int m) {
	for(int i = 0; i < n; i++) {
		int mx = 0;
		for(int j = 0; j < m; j++)
			if(lawn[i][j] > mx)
				mx = lawn[i][j];
		maxr[i] = mx;
	}
	for(int i = 0; i < m; i++) {
		int mx = 0;
		for(int j = 0; j < n; j++)
			if(lawn[j][i] > mx)
				mx = lawn[j][i];
		maxc[i] = mx;
	}

	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			if(maxr[i] > lawn[i][j] && maxc[j] > lawn[i][j])
				return false;
	return true;
}

int main() {
	int t, n, m;
	cin >> t;
	for(int i = 0; i < t; i++) {
		cin >> n >> m;
		for(int j = 0; j < n; j++)
			for(int k = 0; k < m; k++)
				cin >> lawn[j][k];
		if(processOne(n, m))
			printf("Case #%d: YES\n", i + 1);
		else
			printf("Case #%d: NO\n", i + 1);
	}
	return 0;
}