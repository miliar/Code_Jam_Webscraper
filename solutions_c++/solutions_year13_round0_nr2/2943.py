#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <time.h>
using namespace std;

int main()
{
	int t;
	cin >> t;
	
	for (int c = 1; c <= t; ++c) {
		int n, m;
		cin >> n >> m;
		int l[n][m];
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) cin >> l[i][j];
		}
		
		int ok[n][m];
		memset(ok, 0, sizeof(ok) );
		for (int i = 0; i < n; ++i) {
			int maxl = 0;
			for (int j = 0; j < m; ++j) maxl = max(maxl, l[i][j]);
			for (int j = 0; j < m; ++j) if (l[i][j] == maxl) ok[i][j] = true;
		}
		for (int j = 0; j < m; ++j) {
			int maxl = 0;
			for (int i = 0; i < n; ++i) maxl = max(maxl, l[i][j]);
			for (int i = 0; i < n; ++i) if (l[i][j] == maxl) ok[i][j] = true;
		}
		
		bool ok_all = true;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) if (ok[i][j] == 0) ok_all = false;
		}
		
		if (ok_all) printf("Case #%d: YES\n", c);
		else printf("Case #%d: NO\n", c);
	}
	
	return 0;
}
