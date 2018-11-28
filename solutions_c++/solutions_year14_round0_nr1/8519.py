#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <memory.h>

using namespace std;
#define forn(i, n) for(int i = 0; i < (int) n; ++i)
#define fore(i, a, b) for(int i = (int) a; i < (int) b; ++i)
#define pb push_back
#define ld long double
const int MAXN = 200000;

vector <int> v[2];//, ans[3];

int ans[MAXN];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tk;
	cin >> tk;
	forn(q, tk) {
		int c;
		int a[20];
		vector <int> ans;
	    ans.clear();
        memset(a, 0, sizeof a);
	
		forn(k, 2) {
			cin >> c;
			forn(i, 4) {
				forn(j, 4) {
					int x;
					cin >> x;
					if (i == c - 1) {
						a[x]++;
						if (a[x] == 2) ans.pb(x);
					}
				}
			}
		}
        if (ans.size() > 1) {
    		printf("Case #%d: Bad magician!\n", q + 1);
        }

        if (ans.size() == 1) {
     		printf("Case #%d: %d\n", q + 1, ans[0]);
        }

        if (ans.size() == 0) {
    		printf("Case #%d: Volunteer cheated!\n", q + 1);
        }
	}

	return 0;
}
