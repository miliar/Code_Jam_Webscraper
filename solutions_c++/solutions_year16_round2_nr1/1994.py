#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <bitset>
#include <vector>
#include <string>
#include <cstdio>
#include <string>
#include <fstream>
#include <sstream>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define PB push_back
#define SIZE(x) (int)x.size()
#define MP(x, y) make_pair(x, y)
#define ALL(t) (t).begin(),(t).end()
#define CLR(x, y) memset(x, y, sizeof(x))
#define FOR(i, n, m) for (int i = n; i <= m; i++)
#define ROF(i, n, m) for (int i = n; i >= m; i--)

#define RI(x) scanf ("%d", &(x))
#define RII(x, y) RI(x), RI(y)
#define RIII(x, y, z) RI(x), RI(y), RI(z)

typedef long long ll;
typedef unsigned int ui;
typedef unsigned long long ull;

const ll mod = 1e9 + 7;
const int seed = 3;
const double eps = 1e-8;

/***********************END OF DEFINE******************************/

int t;
string s;

int cnt[26];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("data.out", "w", stdout);
    RI(t);
    FOR (i, 0, t - 1) {
        cin >> s;
        CLR(cnt, 0);
        FOR (j, 0, s.size() - 1) {
            cnt[s[j]-'A'] ++;
        }
        //FOR (j, 0, 25) cout << cnt[j] << " "; cout << endl;
        vector<int> res;
        res.clear();
        int nn;
        if(cnt['Z'-'A'] > 0) {
            nn = cnt['Z'-'A'];
            FOR (j, 1, nn) res.push_back(0);
            cnt['Z'-'A'] -= nn;
            cnt['E'-'A'] -= nn;
            cnt['R'-'A'] -= nn;
            cnt['O'-'A'] -= nn;
        }
        if(cnt['W'-'A'] > 0) {
            nn = cnt['W'-'A'];
            FOR (j, 1, nn) res.push_back(2);
            cnt['T'-'A'] -= nn;
            cnt['W'-'A'] -= nn;
            cnt['O'-'A'] -= nn;
        }
        if(cnt['U'-'A'] > 0) {
            nn = cnt['U'-'A'];
            FOR (j, 1, nn) res.push_back(4);
            cnt['F'-'A'] -= nn;
            cnt['O'-'A'] -= nn;
            cnt['U'-'A'] -= nn;
            cnt['R'-'A'] -= nn;
        }
        if(cnt['X'-'A'] > 0) {
            nn = cnt['X'-'A'];
            FOR (j, 1, nn) res.push_back(6);
            cnt['S'-'A'] -= nn;
            cnt['I'-'A'] -= nn;
            cnt['X'-'A'] -= nn;
        }
        if(cnt['R'-'A'] > 0) {
            nn = cnt['R'-'A'];
            FOR (j, 1, nn) res.push_back(3);
            cnt['T'-'A'] -= nn;
            cnt['H'-'A'] -= nn;
            cnt['R'-'A'] -= nn;
            cnt['E'-'A'] -= 2 * nn;
        }
        if(cnt['O'-'A'] > 0) {
            nn = cnt['O'-'A'];
            FOR (j, 1, nn) res.push_back(1);
            cnt['O'-'A'] -= nn;
            cnt['N'-'A'] -= nn;
            cnt['E'-'A'] -= nn;
        }
        if(cnt['T'-'A'] > 0) {
            nn = cnt['T'-'A'];
            FOR (j, 1, nn) res.push_back(8);
            cnt['E'-'A'] -= nn;
            cnt['I'-'A'] -= nn;
            cnt['G'-'A'] -= nn;
            cnt['H'-'A'] -= nn;
            cnt['T'-'A'] -= nn;
        }
        if(cnt['F'-'A'] > 0) {
            nn = cnt['F'-'A'];
            FOR (j, 1, nn) res.push_back(5);
            cnt['F'-'A'] -= nn;
            cnt['I'-'A'] -= nn;
            cnt['V'-'A'] -= nn;
            cnt['E'-'A'] -= nn;
        }
        if(cnt['S'-'A'] > 0) {
            nn = cnt['S'-'A'];
            FOR (j, 1, nn) res.push_back(7);
            cnt['S'-'A'] -= nn;
            cnt['E'-'A'] -= nn;
            cnt['V'-'A'] -= nn;
            cnt['E'-'A'] -= nn;
            cnt['N'-'A'] -= nn;
        }
        if(cnt['I'-'A'] > 0) {
            nn = cnt['I'-'A'];
            FOR (j, 1, nn) res.push_back(9);
            cnt['N'-'A'] -= nn;
            cnt['I'-'A'] -= nn;
            cnt['N'-'A'] -= nn;
            cnt['E'-'A'] -= nn;
        }
        //FOR (j, 0, 25) cout << cnt[j] << " "; cout << endl;
        sort(res.begin(), res.end());
        cout << "Case #" << i + 1 << ": ";
        FOR (j, 0, res.size() - 1) cout << res[j];
        cout << endl;
    }
    return 0;
}
