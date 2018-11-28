#pragma comment (linker, "/STACK:128000000")
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <cassert>

#define mp make_pair
#define pb push_back
#define sz(x) ((int)(x).size())
#define forn(i, n) for(int i=0;i<(n);++i)
#define clr(ar, val) memset(ar, val, sizeof(ar))

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int N = 1e5 + 200;
const int INF = int(1e9);
const long long LINF = 1ll * INF * INF;
const int md = int(1e9) + 7;
const ld eps = 1e-10;
const ld PI = 3.1415926535897932384626433832795l;

int test, it;
int k, l, s;
string target, key;
int pref[111][26];
int p[111];
long double dp[111][111][111], ans, mult[26];
int cnt[26];

int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    cin >> test;
    for (it = 1; it <= test; it++) {
        cin >> k >> l >> s;
        cin >> key;
        cin >> target;

        clr(cnt, 0);
        for (int i = 0; i < key.length(); i++) cnt[key[i] - 'A']++;
        for (int i = 0; i < 26; i++) {
            mult[i] = 1.0 * cnt[i] / k;
            //printf("%.10lf\n", (double)mult[i]);
        }

        int n = target.length();
        clr(p, 0);
        p[0] = 0;
        for (int i = 1; i < n; i++) {
            int j = p[i - 1];
            while (j && target[i] != target[j]) j = p[j - 1];
            if (target[i] == target[j]) j++;
            p[i] = j;
        }

        //for (int i = 0; i < n; i++) printf("%d\n", p[i]);

        clr(pref, 0);

        for (int i = 0; i < 26; i++) {
            pref[0][i] = 0;
            if (i == (target[0] - 'A')) pref[0][i]++;
        }

        for (int i = 1; i <= n; i++)
            for (int j = 0; j < 26; j++) {
                if (i < n) {
                    if (j == (target[i] - 'A')) {
                        pref[i][j] = i + 1;
                        continue;
                    }
                    pref[i][j] = pref[p[i - 1]][j];
                }
                pref[i][j] = pref[p[i - 1]][j];
        }

     //   for (int i = 0; i < n; i++) {
     //       for (int j = 0; j < 26; j++) cout << pref[i][j] << " ";
     //       printf("\n");
     //   }

        clr(dp, 0);
        dp[0][0][0] = 1.0;
        for (int i = 0; i < s; i++)
            for (int j = 0; j < s; j++)
                for (int pp = 0; pp <= l; pp++)
                if (dp[i][j][pp] > eps)
                    for (int choice = 0; choice < 26; choice++)
                    if (cnt[choice]) {
                        int newp = pref[pp][choice];
                        if (newp == l)
                            dp[i + 1][j + 1][newp] += dp[i][j][pp] * mult[choice];
                        else
                            dp[i + 1][j][newp] += dp[i][j][pp] * mult[choice];
                    }
        ans = 0;
        for (int j = 0; j <= s; j++)
            for (int pp = 0; pp <= l; pp++) ans += dp[s][j][pp] * j;


        int mx = 0;
        int curpref = 0;
        for (int i = 0; i < s; i++) {
            int tmp = 0;
            for (int j = 0; j < 26; j++)
            if (cnt[j]) tmp = max(tmp, pref[curpref][j]);
            curpref = tmp;
            if (tmp == l) mx++;
        }

        ans = mx - ans;

        printf("Case #%d: ", it);
        printf("%.12lf\n", (double)ans);
    }
    return 0;
}
