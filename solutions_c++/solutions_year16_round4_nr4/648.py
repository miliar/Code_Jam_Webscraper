#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>

#define mp make_pair
#define pb push_back

#define REP(i, n) for(int i = 0; i < (n); ++i)
#define REP2(i, s, n) for (int i = (s); i < (n); ++i)

using namespace std;
typedef long long ll;

int N;
int dy[40][40] = {0, };
string abil[30];

int go(int machine, int person) {
    if (dy[machine][person] != -2) {
        return dy[machine][person];
    }

    int min_val = 0;
    int cnt_m = 0;
    int cnt_p = 0;

    REP(i, N) {
        if ((1 << i) & machine) ++cnt_m;
        if ((1 << i) & person) ++cnt_p;
    }
    if(cnt_m != cnt_p) return -1;

    REP(i, N) {
        int mc = (1 << i) & machine;
        REP(j, N) {
            int pc = (1 << j) & person;
            if (abil[i][j] == '1') {
                if ((mc && !pc) || (!mc && pc)) {
                    /*
                    cout << machine << " " << person << endl;
                    cout << i << " " << j << endl;
                    cout << "AH!" << endl;
                    */
                    dy[machine][person] = -1;
                    return -1;
                }
            }
            else {
                if (mc && pc) ++min_val;
            }
        }
    }

    REP(i, (1 << N)) {
        REP(j, (1 << N)) {
            if (i == machine || j == person) continue;
            if (i == 0 || j == 0) continue;
            if (((i | machine) == machine) && ((j | person) == person)) {
                int val0 = go(i, j);
                int val1 = go(machine & (~i), person & (~j));
                if(val0 >= 0 && val1 >= 0) {
                    min_val = min(val0 + val1, min_val);
                }
            }
        }
    }

    //cout << machine << " " << person << " : " << min_val << endl;

    dy[machine][person] = min_val;
    return min_val;
}

void solve()
{
    cin >> N;
    REP(i, N) {
        cin >> abil[i];
    }
    REP(i, 40) REP(j, 40) dy[i][j] = -2;
    cout << go((1 << N)-1, (1 << N)-1) << endl;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}

	return 0;
}
