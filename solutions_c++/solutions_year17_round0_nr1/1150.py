#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <iostream>

using namespace std;
#define dprintf debug && printf
#define F(x,y) for(typeof((y).begin()) x = (y).begin(); x != (y).end(); ++x) 
#define CHECKREAD(x, ...) if(scanf(__VA_ARGS__) != x) { fprintf(stderr, "Failed to read on %s, %d\n", __FILE__, __LINE__); exit(1); }


const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

bool solve(int P) {
	printf("Case #%d: ", P+1);
	string S;
	int K, ret = 0;
	cin >> S >> K;
	for(int i = 0; i < S.size() - K + 1; ++i) {
		if(S[i] == '-') {
			++ret;
			for(int k = 0; k < K; ++k) {
				S[i + k] = S[i+k] == '-' ? '+' : '-';
			}
		}
	}
	if(find(S.begin(), S.end(), '-') != S.end()) {
		cout << "IMPOSSIBLE" << endl;
	} else {
		cout << ret << endl;
	}
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
