#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("C.txt", "w", stdout);
	int T;

	cin >> T;
	for (int tc = 1 ; tc <= T ; tc ++){
		string S;
		int K, p = 0, ans = 0;

		cin >> K >> S;
		for (int i = 0 ; i < (int)S.size() ; i ++){
            int pp = (S[i]-'0');
            if (i > p) ans += i-p, p += i-p;
            p += pp;
		}

		printf("Case #%d: %d\n", tc, ans);
	}
    cin >> T;
	return 0;
}
