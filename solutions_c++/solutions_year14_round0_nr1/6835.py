#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

int sqr[5][5], from[17], from1[17];

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout); 

	int t, tt = 0, a1, a2; 
	cin >> t;

	while (t--) {
		printf("Case #%d: ", ++ tt); 
		cin >> a1;
		for (int i = 1; i <= 4; ++ i) {
			for (int j = 1; j <= 4; ++ j) {
				cin >> sqr[i][j]; 
				from[sqr[i][j]] = i; 
			}
		}

		cin >> a2;
		for (int i = 1; i <= 4; ++ i) {
			for (int j = 1; j <= 4; ++ j) {
				cin >> sqr[i][j]; 
				from1[sqr[i][j]] = i; 
			}
		}

		int ans = 0, end = 0;

		for (int i = 1; i <= 16; ++ i) {
			if (end) break; 
			if (from[i] == a1 && from1[i] == a2) {
				if (ans) {end = 1; printf("Bad magician!\n"); continue; }
				ans = i; 
			}
		}

		if (ans && ! end) printf("%d\n", ans);
		else if (! end) printf("Volunteer cheated!\n"); 

	}
}