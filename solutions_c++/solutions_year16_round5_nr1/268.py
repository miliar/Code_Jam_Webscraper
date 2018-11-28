// In the name of God

#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <deque>
#include <assert.h>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <stdio.h>
#include <string.h>
#include <utility>
#include <math.h>
#include <bitset>
#include <iomanip>

using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; ++i)

const int N = 0, mod = 0;

/**/
#define cin fin
#define cout fout
/**/
ifstream fin("xx.in");
ofstream fout("res.out");

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int tc;
    cin >> tc;
    for (int tn = 1; tn <= tc; ++tn) {
        cout << "Case #" << tn << ": ";
        string s;
        cin >> s;
        int n = (int) s.size();
        int res = 0, cnt = 0, cur = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (cnt && cur == s[i]) {
                cnt--;
                cur = 'J' + 'C' - cur;
                res += 10;
            } else {
                cnt++;
                cur = s[i];
            }
        }
        res += (cnt / 2) * 5;
        cout << res << '\n';
    }
}







