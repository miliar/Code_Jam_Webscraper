#include <bits/stdc++.h>
using namespace std;
#define FOR(i, a, b) for(int i = int(a); i < int(b); ++i)
#define FORR(i, n) FOR(i, 0, n)
#define sz(a) int((a).size())

int main() {
	int maior, res, origin, t;
	scanf("%d", &t);
	FOR(k, 1, t+1) {
		char c;
		scanf(" %d", &maior);
		res = origin = 0;
		FORR(i, maior+1) {
			scanf(" %c", &c);
			origin += c-'0';
			if( res < i ) res = i;
			res += c-'0';
		}
		printf("Case #%d: %d\n", k, res-origin);
	}
}
