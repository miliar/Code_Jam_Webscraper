#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("outputLarge.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int test = 1; test<=t; test++) {
		int n;
		string audience;
		cin >> n >> audience;
		int q = 0;
		int r = 0;
		for(int i = 0; i<(int)audience.size(); i++) {
			int ni = audience[i] - '0';
			int aux = max(0, i-q); 
			r += aux;
			q += aux;
			q += ni;
		}
		printf("Case #%d: %d\n", test, r);
	}
	return 0;
}