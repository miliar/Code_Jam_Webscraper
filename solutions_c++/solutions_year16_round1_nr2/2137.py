#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int casenum = 1; casenum <= T; ++casenum) {
        int N;
        cin >> N;
        vector<vector<int>> lists;
        forn(i, 2*N - 1) {
            vector<int> list(N);
            forn(i, N) cin >> list[i];
            lists.push_back(list);
        }
        vector<int> res;
        vector<bool> done(2*N-1);
        forn(n, N) {
            int m = 25600;
            vector<int> v;
            forn(j, 2*N-1) if (!done[j]) {
                v.push_back(lists[j][n]);
                m = min(m, lists[j][n]);
            }
            vector<int> mins;
            forn(j, 2*N-1) if (!done[j] && lists[j][n] == m) mins.push_back(j);
            for (int m : mins) for(int j = n; j < N; ++j) {
                v.push_back(lists[m][j]);
            }
            /* for(auto l : v) cout << l << ' '; */
            /* cout << endl; */
            sort(v.begin(), v.end());
            const int x = v.size();
            int j = 0;
            if (mins.size() == 1) {
                res.push_back(lists[mins[0]][n]);
            }
            for(int j = 0; j < x; ++j) {
                if (v[j] != v[j+1]) {
                    res.push_back(v[j]);
                } else {
                    ++j;
                }
            }

            for (auto m : mins) done[m] = true;
        }
        cout << "Case #" << casenum << ':';
        forn(i, N) cout << ' ' << res[i];
        cout << endl;
	}
	return 0;
}

