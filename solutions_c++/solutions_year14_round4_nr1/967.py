#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
using namespace std;


int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		printf("Case #%d:", cas);
		int N, X;
		scanf("%d %d", &N, &X);
		multiset<int> s;
		for (int i = 0; i < N; ++i) {
			int S;
			scanf("%d", &S);
			s.insert(S);
		}
		int ans = 0;
		while(!s.empty()) {
			multiset<int>::iterator it = --s.end();
			int val = *it;
			s.erase(it);
			it = s.upper_bound(X - val);
			if (it != s.begin()) {
				s.erase(--it);
			}
			++ans;
		}
		printf(" %d\n", ans);
	}
	return 0;
}
