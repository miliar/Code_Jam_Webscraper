#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main()
{
	int T;
	cin >> T;
	cout.precision(8);
	for (int casenum = 1; casenum <= T; ++casenum) {
        long long K, C, S;
        cin >> K >> C >> S;
        cout << "Case #" << casenum << ":";
        if (S*C < K) {
            cout << " IMPOSSIBLE" << endl;
            continue;
        }
        for (int k = 0; k < K; ++k) {
            long long i = (long long)k;
            for (int c = 1; c < C; ++c) {
                i *= K;
                ++k;
                if (k < K) i += k;
            }
            cout << ' ' << (i+1);
        }
        cout << endl;
	}
	return 0;
}

