#include <bits/stdc++.h>

#define FOR(i,a,b) for (int i=a; i<b; i++)
#define REP(i,a) FOR(i,0,a)

typedef long long ll;
typedef unsigned long long int ulli;

using namespace std;

#define LIM 100

int main() {
	int T, N, tmp; 
	string str;
	cin >> T;
	REP(test, T) {
		cin >> N;
		cin >> str;

		int storage = 0, ans = 0;
		REP(i, N+1) {
			tmp = str[i] - '0';
			if (tmp) {
				storage += tmp - 1;
			} else {
				if (storage) {
					storage--;
				} else {
					ans++;
				}
			}
		}

		printf("Case #%d: %d\n", test + 1, ans);
	}

	return 0;
}	