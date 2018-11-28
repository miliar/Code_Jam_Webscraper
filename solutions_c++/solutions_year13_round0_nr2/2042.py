//Copyright (c) Nguyen Nam
#pragma comment(linker, "/STACK:0x04000000")
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <cassert>
#include <climits>
#include <ctime>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>

using namespace std;
typedef unsigned int uint;
typedef long long i64;
typedef unsigned long long ui64;
typedef long double ld;

int Count(const vector<vector<int>> &lawn, int j, int n, int h) {
    int res = 0;
    for (int i = 0; i < n; i++) {
        res += lawn[i][j] == h;
    }
    return res;
}

string Sol(const vector<vector<int>> &lawn) {
    int n = lawn.size();
    int m = lawn.front().size();
    vector<vector<int>> tmp_lawn(n, vector<int>(m, 100));
    vector<bool> us_hor(n);
    vector<bool> us_ver(m);
    for (int h = 100; h >= 1; h--) {
        for (int i = 0; i < n; i++) {
            if (us_hor[i]) {
                continue;
            }
            if (count(lawn[i].begin(), lawn[i].end(), h) != 0) {
                us_hor[i] = true;
            }
            tmp_lawn[i] = vector<int>(m, h);
        }
        for (int j = 0; j < m; j++) {
            if (us_ver[j]) {
                continue;
            }
            if (Count(lawn, j, n, h) != 0) {
                us_ver[j] = true;
            }
            for (int i = 0; i < n; i++) {
                tmp_lawn[i][j] = h;
            }
        }
    }
    return tmp_lawn == lawn ? "YES" : "NO";
}

int main() {
#ifdef NOVACO
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int i_t = 1; i_t <= t; i_t++) {
        int n;
        int m;
        cin >> n >> m;
        vector<vector<int>> lawn(n, vector<int>(m));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> lawn[i][j];
            }
        }
        string res = Sol(lawn);
        cout << "Case #" << i_t << ": " << res << "\n";
    }
}