#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <bitset>
#include <queue>
#include <map>


using namespace std;


vector<pair<int, pair<int, int> > > v;
int ans = 0;
int sum = 0;
int cnt[10][10];
int cnt1[10][10];
int k;
int cnt2[10][10];
vector<pair<int, pair<int, int> > > cur, anss;


void get(int i) {
    if (i == (int)v.size()) {
        ans = max(ans, sum);
        if (ans == sum) {
            anss = cur;
        }
        return;
    }
    get(i + 1);
    int a = v[i].first;
    int b = v[i].second.first;
    int c = v[i].second.second;
    if (cnt[a][b] < k && cnt1[a][c] < k && cnt2[b][c] < k) {
        cnt[a][b]++;
        sum++;
        cnt1[a][c]++;
        cnt2[b][c]++;
        cur.push_back(v[i]);
        get(i + 1);
        cur.pop_back();
        cnt[a][b]--;
        sum--;
        cnt1[a][c]--;
        cnt2[b][c]--;
    }
}


int main() {
    freopen("twopaths.in", "r", stdin);
    freopen("twopaths.out", "w", stdout);
    int t;
    cin >> t;
    for (int ii = 0; ii < t; ii++) {
        int j, p, s;
        cin >> j >> p >> s >> k;
        if (k >= s) {
            cout << "Case #" << ii + 1 << ':' << ' ' << j * p * s << endl;
            for (int i = 1; i <= j; i++) {
                for (int g = 1; g <= p; g++) {
                    for (int h = 1; h <= s; h++) {
                        cout << i << ' ' << g << ' ' << h << endl;
                    }
                }
            }
            continue;
        }
        v.clear();
        for (int i = 1; i <= j; i++) {
            for (int g = 1; g <= p; g++) {
                for (int h = 1; h <= s; h++) {
                    v.push_back(make_pair(i, make_pair(g, h)));
                }
            }
        }   
        ans = 1;
        sum = 0;
        get(0);
        cout << "Case #" << ii + 1 << ':' << ' ' << ans << endl;
        for (int i = 0; i < ans; i++) {
            cout << anss[i].first << ' ' << anss[i].second.first << ' ' << anss[i].second.second << endl;
        }
    }
    return 0;
}
