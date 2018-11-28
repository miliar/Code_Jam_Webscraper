#include<iostream>
using namespace std;

bool check(int g[101][101], int m, int n) {
	for(int j = 0; j < m; ++j) {
		for(int k = 0; k < n; ++k) {
			if(g[j][k] != min(g[j][100], g[100][k])) {
				return false;
			}
		}
	}
	return true;
}

int main() {
	int test, m, n, g[101][101];
	cin>>test;
	for(int i = 0; i < test; ++i) {
		cin>>m>>n;
		for(int j = 0; j < 100; ++j) {
			g[100][j] = g[j][100] = 1;
		}
		for(int j = 0; j < m; ++j) {
			for(int k = 0; k < n; ++k) {
				cin>>g[j][k];
				if(g[j][k] > g[100][k]) {
					g[100][k] = g[j][k];
				}
				if(g[j][k] > g[j][100]) {
					g[j][100] = g[j][k];
				}
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(check(g, m, n)) {
			cout<<"YES"<<endl;
		} else {
			cout<<"NO"<<endl;
		}
	}
	return 0;
}