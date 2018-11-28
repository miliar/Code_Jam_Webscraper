#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main()
{
	int T;
	cin >> T;
	cout.precision(8);
	for (int casenum = 1; casenum <= T; ++casenum) {
        int N;
        cin >> N;
        vector<bool> seen(10);
        int cnt = 0;
        int r = -1;
        for(int i = 1; i < 1000; ++i) {
            long long x = (long long)i*N;
            while (x > 0) {
                if (seen[x%10] == false) ++cnt;
                seen[x%10] = true;
                x /= 10;
            }
            if (cnt == 10) {
                r = i*N;
                break;
            }
        }
		cout << "Case #" << casenum << ": ";
        if (r >= 0) {
            cout << r << endl;
        } else {
            cout << "INSOMNIA" << endl;
        }
	}
	return 0;
}

