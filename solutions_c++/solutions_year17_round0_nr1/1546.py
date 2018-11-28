#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

void solve()
{
    string str;
    int k;
    cin >> str >> k;
    int ret = 0;
    for(int i = 0; i + k <= str.size(); ++ i) {
        if (str[i] == '-') {
            ret ++;
            for(int j = 0; j < k; ++ j) {
                if (str[i + j] == '-') str[i + j] = '+';
                else str[i + j] = '-';
            }
        }
    }
    for(int i = 0; i < str.size(); ++ i) {
        if (str[i] == '-') {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << ret << endl;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d: ", i + 1);
		cerr << "Start: " << i << endl;
		solve();
	}
	return 0;
}
