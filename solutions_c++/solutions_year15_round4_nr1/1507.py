#include <iostream>
using namespace std;

char c[110][110];
int a[110][110];

int rozwiaz(int t) {
	int n, m;
	int odp = 0;
	cin >> n >> m;
	for(int i = 0; i < n; i ++) {
		for(int j = 0; j < m; j ++) {
			cin >> c[i][j];
			a[i][j] = 1;
		}
	}
	for(int i = 0; i < n; i ++) {
		for(int j = 0; j < m; j ++) {
			if(c[i][j] != '.') {
				a[i][j] *= 2;
				break;
			}
		}
	}
	
	for(int i = 0; i < n; i ++) {
		for(int j = m - 1; j >= 0; j --) {
			if(c[i][j] != '.') {
				a[i][j] *= 3;
				break;
			}
		}
	}
	for(int j = 0; j < m; j ++) {
		for(int i = 0; i < n; i ++) {
			if(c[i][j] != '.') {
				a[i][j] *= 5;
				break;
			}
		}
	}
	for(int j = 0; j < m; j ++) {
		for(int i = n - 1; i >= 0; i --) {
			if(c[i][j] != '.') {
				a[i][j] *= 7;
				break;
			}
		}
	}
	
	/*for(int i = 0; i < n; i ++) {
		for(int j = 0; j < m; j ++) 
			cout << a[i][j] << " ";
			cout << endl;
	}*/
	for(int i = 0; i < n; i ++) {
		for(int j = 0; j < m; j ++) {
			if(a[i][j] == 210) {
				return -1;
			}
			if(a[i][j] % 2 == 0 && c[i][j] == '<') {
				odp ++;
			}
			if(a[i][j] % 3 == 0 && c[i][j] == '>') {
				odp ++;
			}
			if(a[i][j] % 5 == 0 && c[i][j] == '^') {
				odp ++;
			}
			if(a[i][j] % 7 == 0 && c[i][j] == 'v') {
				odp ++;
			}
		}
	}
	
	
	return odp;
}

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; i ++) {
		int a = rozwiaz(t);
		if(a < 0) 
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i << ": " << a << endl;
	}
}
