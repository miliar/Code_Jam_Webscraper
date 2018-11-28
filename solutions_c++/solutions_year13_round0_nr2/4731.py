#include<cstdio>
#include<iostream>
#include<algorithm>
using std::cin;
using std::cout;
using std::endl;
using std::max;

int gp[105][105],c[105],r[105],n,m;
bool check() {
	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++){
			if(gp[i][j] < c[i] && gp[i][j] < r[j])
				return false;
		}
	return true;
}

int main () {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin >> T;
	for(int cas = 1; cas <= T; cas++) {
		cin >> n >> m;
		for(int i = 0; i< n; i++) {
			for(int j = 0; j < m; j++)
				cin >> gp[i][j];
		}
		for(int i = 0; i < n; i++) {
			c[i] = gp[i][0];
			for(int j = 0; j < m; j++) {
				c[i] = max(c[i],gp[i][j]);
			}
		}
		for(int i = 0; i < m; i++) {
			r[i] = gp[0][i];
			for(int j = 0; j < n; j++) {
				r[i] = max(r[i],gp[j][i]);
			}
		}
		cout << "Case #" << cas << ": ";
		if(check()) 
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}
