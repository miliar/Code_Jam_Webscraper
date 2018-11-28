#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

int main() {
	FILE *fin = freopen("D-small.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("D-small.out", "w", stdout);
	int T;
	cin >> T;
	bool first = true;
	for (int t = 1; t <= T; t++){
		if (first) first = false;
		else cout << endl;
		cout << "Case #" << t << ": ";
		
		int k, c, s;
		cin >> k >> c >> s;
		if (k == 1) cout << 1;
		else if (c == 1 && s < k) cout << "IMPOSSIBLE";
		else if (s < k - 1) cout << "IMPOSSIBLE";
		else if (c == 1){
			for (int i = 1; i < k; i++){
				cout << i << " ";
			}
			cout << k;
		}
		else{
			int start = 0;
			for (int i = 2; i < k; i++){
				cout << i << " ";
			}
			cout << k;
		}
	}
	exit(0);
}