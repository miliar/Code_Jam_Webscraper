#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
#include <stdio.h>
using namespace std;

#define RT freopen("a.in", "r", stdin)
#define WT freopen("b.out", "w", stdout)
#define LL long long int
#define MAX 100
#define MAXSZ 1000000

string Inp;
int N;

bool check(char c) {
	return !(c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'a');
}

int Solve() {
	int ret = 0;
	for(int i = 0; i < Inp.size(); ++i) {
		for(int j = i; j < Inp.size(); ++j) {
			int count = 0;
			for(int k = i; k <= j; ++k) {
				if(check(Inp[k])) {
					++count;
				}
				else {
					if(count >= N) {
						++ret;
						count = 0;
						break;
					}
					count = 0;
				}
			}
			if(count >= N) ++ret;
		}
	}
	return ret;
}

int main() {
	RT, WT;
	int cases, res; cin >> cases;
	for(int c = 0; c < cases; ++c) {
		cin >> Inp >> N;
		res = Solve();
		printf("Case #%d: %d\n", c + 1, res);
	}
	return 0;
}