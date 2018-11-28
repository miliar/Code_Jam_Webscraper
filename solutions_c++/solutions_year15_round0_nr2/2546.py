#pragma comment(linker, "/STACK:6400000000000")

#define _USE_MATH_DEFINES

#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
#include <stack>
#include <bitset>
using namespace std;

typedef long long ll;
typedef long double ld;

const ld EPS = 1e-12;
const int INF = (int)(2e9 + 0.5);
const int MAXN = 300;

/*
int dfs(vector<int> v, int time = 0) {

    int flag = false;

    for(int i = 0; i < (int)v.size(); ++i)
        flag |= (v[i] > 0);

    if(!flag) return time;

    vector<int> vv;
    for(int i = 0; i < (int)v.size(); ++i)
        vv.push_back(v[i] - 1);

    int timeNow = dfs(vv, time + 1);

    for(int i = 0; i < (int)vv.size(); vv[i]++, ++i);

    for(int i = 0; i < (int)vv.size(); ++i) {
        for(int j = 1; j < vv[i]; ++j) {
            vv[i] -= j;
            vv.push_back(j);
            timeNow = min(timeNow, dfs(vv, time + 1));
            vv[i] += j;
            vv.pop_back();
        }
    }

    if(timeNow == 5) {
        for(int i = 0; i < (int)v.size(); cout << v[i] << " ", ++i);
        cout << endl;
    }

    return timeNow;
}

int t, n, a;
vector<int> v;

int main() {
    freopen("INPUT.TXT", "r", stdin);
    //freopen("OUTPUT.TXT", "w", stdout);
    scanf("%d", &t);
    for(int q = 1; q <= t; ++q) {
        v.clear();
        scanf("%d", &n);
        for(int i = 0; i < n; scanf("%d", &a), v.push_back(a), ++i);
        printf("Case #%d: %d\n", q, dfs(v));
    }
}

*/


int t, d, a, ans;
vector<int> v;

int main() {
    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);
    scanf("%d", &t);
    for(int w = 1; w <= t; ++w) {
        v.clear();
        ans = INF;
        scanf("%d", &d);
        for(int i = 0; i < d; ++i) {
            scanf("%d", &a);
            v.push_back(a);
        }
        for(int i = 0; i < (1 << d); ++i) {
            int mmax = 0;
            int splits = __builtin_popcount(i);
            for(int j = 0; j < d; ++j) {
                if(i & (1 << j)) {
                    if(v[j] == 9) {
                        mmax = max(mmax, 3);
                        splits++;
                    } else {
                        int y = v[j] / 2;
                        mmax = max(mmax, max(y, v[j] - y));
                    }
                } else
                    mmax = max(mmax, v[j]);
            }
            ans = min(ans, mmax + splits);
        }
        for(int i = 0; i < (1 << d); ++i) {
            int mmax = 0;
            int splits = __builtin_popcount(i);
            for(int j = 0; j < d; ++j) {
                if(i & (1 << j)) {
                    int y = v[j] / 2;
                    mmax = max(mmax, max(y, v[j] - y));
                } else
                    mmax = max(mmax, v[j]);
            }
            ans = min(ans, mmax + splits);
        }
        printf("Case #%d: %d\n", w, ans);
    }
}


/*
const int cost[10] = {0, 1, 2, 3, 3, 4, 4, 5, 5, 6};
int t, d, a, ans;
priority_queue<int> q;

int main() {
    freopen("INPUT.TXT", "r", stdin);
    //freopen("OUTPUT.TXT", "w", stdout);
    scanf("%d", &t);
    for(int w = 1; w <= t; ++w) {
        while(!q.empty()) q.pop();
        scanf("%d", &d);
        for(int i = 0; i < d; ++i) {
            scanf("%d", &a);
            q.push(a);
        }
        ans = q.top();
        int mmax = 0;
        int splits = 0;
        while(!q.empty()) {
            int x = q.top();
            if(x < 4) break;
            q.pop();
            int y = x / 2;
            mmax = max(mmax, max(y, x - y));
            ++splits;
            ans = min(ans, splits + max(mmax, (!q.empty() ? q.top() : 0)));
        }
        printf("Case #%d: %d\n", w, ans);
    }
}
*/
