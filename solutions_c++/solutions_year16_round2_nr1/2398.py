#pragma comment(linker, "/STACK:65777216")
#include <iostream>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <string>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <ctime>
#define pb push_back
#define mp make_pair
#define ll long long

using namespace std;

int main () {
    freopen ("input", "r", stdin);
    freopen ("output", "w", stdout);

    vector<string> a = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

    ll n;
    string s;

    int count[10][1000];

    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < 1000; ++j) {
            count[i][j] = 0;
        }
    }

    for (int i = 0; i < 10; ++i) {
        for (int j = 0; j < a.size(); ++j) {
            ++count[i][a[i][j]];
        }
    }

    cin >> n;
    vector <int> r(1000, 0);

    vector <int> ans(1000, 0);
    int strn;

    for (int t = 0; t < n; ++t) {
        r.assign(1000, 0);
        ans.assign(1000, 0);
        cin >> s;
        for (int i = 0; i < s.size(); ++i) {
            ++r[s[i]];
            if (s[i] == 'Z') {
                strn = 0;
                ++ans[strn];
                for (int j = 0; j < a[strn].size(); ++j) {
                    --r[a[strn][j]];
                }
            }
            if (s[i] == 'W') {
                strn = 2;
                ++ans[strn];
                for (int j = 0; j < a[strn].size(); ++j) {
                    --r[a[strn][j]];
                }
            }
            if (s[i] == 'U') {
                strn = 4;
                ++ans[strn];
                for (int j = 0; j < a[strn].size(); ++j) {
                    --r[a[strn][j]];
                }
            }
            if (s[i] == 'X') {
                strn = 6;
                ++ans[strn];
                for (int j = 0; j < a[strn].size(); ++j) {
                    --r[a[strn][j]];
                }
            }
            if (s[i] == 'G') {
                strn = 8;
                ++ans[strn];
                for (int j = 0; j < a[strn].size(); ++j) {
                    --r[a[strn][j]];
                }
            }
        }


        while (r['O'] > 0) {
            strn = 1;
            ++ans[strn];
            for (int j = 0; j < a[strn].size(); ++j) {
                --r[a[strn][j]];
            }
        }
        while (r['T'] > 0) {
            strn = 3;
            ++ans[strn];
            for (int j = 0; j < a[strn].size(); ++j) {
                --r[a[strn][j]];
            }
        }
        while (r['F'] > 0) {
            strn = 5;
            ++ans[strn];
            for (int j = 0; j < a[strn].size(); ++j) {
                --r[a[strn][j]];
            }
        }
        while (r['V'] > 0) {
            strn = 7;
            ++ans[strn];
            for (int j = 0; j < a[strn].size(); ++j) {
                --r[a[strn][j]];
            }
        }
        while (r['I'] > 0) {
            strn = 9;
            ++ans[strn];
            for (int j = 0; j < a[strn].size(); ++j) {
                --r[a[strn][j]];
            }
        }


        cout << "Case #" << t + 1 << ": ";
        for (int i = 0; i < 10; ++i) {
            while(ans[i] > 0) {
                --ans[i];
                cout << i;
            }
        }
        cout << endl;
    }
}