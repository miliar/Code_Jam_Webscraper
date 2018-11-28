#include <iostream>
#include <cstdio>
#define LL long long
#define LD long double
#define SIZE 321

using namespace std;

LL T, z;
int w[SIZE][SIZE], n, m, col[SIZE], row[SIZE], ans, i, j, qmax;

int min(int a, int b) {
	if (a < b) return a;
	else return b;
}

int main() {

#if 1
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif

	cin>>T;
	for (z = 1; z <= T; z++) {
		cin>>n>>m;
		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++) cin>>w[i][j];
		
		for (i = 0; i < n; i++) {
			qmax = 0;
			for (j = 0; j < m; j++)
				if (w[i][j] > qmax) qmax = w[i][j];
			row[i] = qmax;
		}
		
		for (j = 0; j < m; j++) {
			qmax = 0;
			for (i = 0; i < n; i++)
				if (w[i][j] > qmax) qmax = w[i][j];
			col[j] = qmax;
		}
		
		ans = 1;
		for (i = 0; i < n; i++)
			for (j = 0; j < m; j++)
				if (w[i][j] != min(row[i], col[j])) ans = 0;
		
		cout<<"Case #"<<z<<": ";
		if (ans) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	return 0;
}
