/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

int t, n;
vector<int> v[30];
map<string, int> mp;
int cnt1[2000], cnt2[2000];

int get_id(const string &s) {
    if (mp.find(s) == mp.end()) {
        mp.insert(make_pair(s, mp.size()));
    }
    return mp[s];
}

void solve() {
    mp.clear();
    scanf("%d", &n);
    string s;
    getline(cin, s);
    for (int i = 0; i < n; ++i) {
        v[i].clear();
        getline(cin, s);
        stringstream ss(s);
        while (ss >> s) {
            v[i].push_back(get_id(s));
        }
    }
    memset(cnt1, 0, sizeof(cnt1));
    memset(cnt2, 0, sizeof(cnt2));
    for (int i = 0; i < v[0].size(); ++i)
        cnt1[v[0][i]]++;
    for (int i = 0; i < v[1].size(); ++i)
        cnt2[v[1][i]]++;
    int res = 0;
    for (int i = 0; i < mp.size(); ++i)
        if (cnt1[i] > 0 && cnt2[i] > 0)
            ++res;
    int ans = INT_MAX;
    for (int s = 0; s < (1 << n); ++s) {
        if ((s & 2) != 2)
            continue;
        int tmp = 0;
        for (int i = 2; i < n; ++i) {
            for (int j = 0; j < v[i].size(); ++j) {
                int cur = v[i][j];
                if (((s >> i) & 1) == 0) {
                    if (cnt1[cur] == 0 && cnt2[cur] > 0) {
                        ++tmp;
                    }
                    ++cnt1[cur];
                } else {
                    if (cnt2[cur] == 0 && cnt1[cur] > 0) {
                        ++tmp;
                    }
                    ++cnt2[cur];
                }
            }
        }
        for (int i = 2; i < n; ++i) {
            for (int j = 0; j < v[i].size(); ++j) {
                int cur = v[i][j];
                if (((s >> i) & 1) == 0) {
                    --cnt1[cur];
                } else {
                    --cnt2[cur];
                }
            }
        }
        ans = min(ans, res + tmp);
    }
    printf("Case #%d: %d\n", ++t, ans);
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
