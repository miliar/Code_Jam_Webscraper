#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main()
{
	int T;
	cin >> T;
	cout.precision(8);
	for (int casenum = 1; casenum <= T; ++casenum) {
        string s;
        cin >> s;
        char l = s[0];
        int cnt = 0;
        for (char c : s) {
            if (c != l) ++cnt;
            l = c;
        }
        if (l == '-') ++cnt;

		cout << "Case #" << casenum << ": " << cnt << endl;
	}
	return 0;
}

