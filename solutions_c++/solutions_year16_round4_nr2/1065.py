#define _CRT_SECURE_NO_WARNINGS

#pragma comment(linker, "/STACK:16777216")
#include <cmath>
#include <math.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <time.h>
#include <iomanip>
#include <cstdio>
#include <complex>

using namespace std;

long double get(vector<long double> a) {
    vector<long double> k(a.size() + 10);
    vector<long double> d(a.size() + 10);
    k[0] = 1;
    for (int i = 0; i < a.size(); i++) {
        for (int j = 0; j < k.size(); j++) d[j] = 0;
        for (int j = 0; j < k.size(); j++) {
            d[j] += k[j] * (1 - a[i]);
            d[j + 1] += k[j] * a[i];
        }
        k = d;
    }
    return k[a.size() / 2];
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; test++) {
        int n, k;
        cin >> n >> k;
        vector<long double> a;
        a.resize(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        vector<int> p(n+1, 0);
        long double ans = 0;
        while (p[n] == 0) {
            vector<long double> d;
            for (int i = 0; i < p.size(); i++) if (p[i] == 1) d.push_back(a[i]);
            if (d.size() == k) {
                ans = max(ans, get(d));
            }
            int i = 0;
            while (p[i] == 1) {
                p[i] = 0;
                i++;
            }
            p[i] = 1;
        }
        cout << fixed << setprecision(8) << "Case #" << test << ": " << ans << endl;
    }
}

