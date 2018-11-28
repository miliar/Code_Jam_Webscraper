#include <bits/stdc++.h>
using namespace std;

int main() {
	int t, smax;
	string vals;
	int p[1001];
	cin >> t;
	for(int i = 0; i<t; i++) {
		int ans = 0, pmax = 0;
		cin>>smax;
		cin>>vals;
		if(smax == 0) {
			printf("Case #%d: 0\n", i+1);
			continue;
		}
		
		for(int j = 0; j <= smax; j++) {
			p[j] = vals[j] - '0';
		}
		
		for(int j = 0; j <= smax; j++) {
			if(j == pmax && p[j] == 0) {
				ans += 1;
				pmax += 1;
				continue;
			}
			pmax += p[j];
			if(pmax >= smax) break;
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
}
