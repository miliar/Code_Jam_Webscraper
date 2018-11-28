#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <cmath>
#include <cstdio>

using namespace std;

int main() {	
//	freopen("B-small-attempt0.in", "r", stdin);

	int T = 0; 
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cerr << t << endl;
		int n,m;
		cin >> n >> m;
		vector< vector<int> > pole(n,vector<int>(m,0));
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				scanf("%d", &pole[i][j]);
			}
		}
		while(1) {
			int mn = 100;
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < m; ++j) {
					if (mn > pole[i][j]) {
						mn = pole[i][j];
					}
				}
			}
			if (mn == 100) {
				std::cout << "Case #" << t << ": YES" << endl; 
				break;
			}
										 
			bool Flag = false;
			for (int i = 0; i < n; ++i) {
				bool flag = true;
				bool fl = false;
				for (int j = 0; j < m; ++j) {
					if (! (pole[i][j] == mn || pole[i][j] == 200) ) {
						flag = false;
					}
					if (pole[i][j] == mn) {
						fl = true;
					}
				}
				if (flag && fl) {
					Flag = true;
					for (int j = 0; j < m; ++j) {
						pole[i][j] = 200;
					}
				}
			}
			for (int j = 0; j < m; ++j) {
				bool flag = true;
				bool fl = false;
				for (int i = 0; i < n; ++i) {
					if (! (pole[i][j] == mn || pole[i][j] == 200) ) {
						flag = false;
					}
					if (pole[i][j] == mn) {
						fl = true;
					}
				}
				if (flag && fl) {
					Flag = true;
					for (int i = 0; i < n; ++i) {
						pole[i][j] = 200;
					}
				}
			}
			if (!Flag) {
		        std::cout << "Case #" << t << ": NO" << endl; 
				break;		
			}
		}

	}
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	return 0;
}
