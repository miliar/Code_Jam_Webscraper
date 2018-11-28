#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	int all = (1 << 10) - 1;
	bool first = true;
	for (int t = 1; t <= T; t++){
		if (first) first = false;
		else cout << endl;
		ULL n;
		cin >> n;
		if (n == 0){
			cout << "Case #" << t << ": INSOMNIA";
			continue;
		}
		ULL i = 1, in = n;
		int seen = 0;
		for (i = 1; seen != all; i++){
			in = i * n;
			while (in){
				seen |= (1 << (in % 10));
				in /= 10;
			}
		}
		cout << "Case #" << t << ": ";
		cout << --i * n;
	}
	exit(0);
}