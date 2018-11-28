#pragma comment(linker, "/STACK:16777216")
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <ctime>
#include <stack>
#include <algorithm>
#include <numeric>
#include <complex>
#include <functional>
#include <list>
#include <iostream>
using namespace std;

#define X first
#define Y second
#define pb push_back
#define ppb pop_back
#define mp make_pair

typedef long long i64;

const double EPS = 1e-6;
const int INF = ~(1 << 31);
const i64 LINF = ~(1LL << 63);

#define sqr(x) (x)*(x)

// stuff cutline

int string_to_int(string s) {
    int ten = 1, res = 0;
    for(int i = s.size() - 1; i >= 0; i--) {
        res += (s[i] - '0') * ten;
        ten *= 10;
    }
    return res;
}

vector<int> z_function (string s) {
    int n = (int) s.length();
    vector<int> z (n);
    for (int i=1, l=0, r=0; i<n; ++i) {
        if (i <= r)
            z[i] = min (r-i+1, z[i-l]);
        while (i+z[i] < n && s[z[i]] == s[i+z[i]])
            ++z[i];
        if (i+z[i]-1 > r)
            l = i,  r = i+z[i]-1;
    }
    return z;
}

//int d[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

bool check(vector<char> used) {
    for (int i = 0; i < used.size(); i++) {
        if (used[i] == 0) {
            return false;
        }
    }
    return true;
}

int main(){
#ifndef _DEBUG
    /*freopen("strings.in", "r", stdin);
     freopen("strings.out", "w", stdout);*/
#endif
    freopen("/users/zakhar/documents/xcode projects/olymp/olymp/olymp/A-large.in", "r", stdin);
    freopen("/users/zakhar/documents/xcode projects/olymp/olymp/olymp/output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int t;
    i64 n;
    cin >> t;
    for (int k = 1; k <= t; k++) {
        cin >> n;
        int it = 1;
        i64 cur = n;
        bool found = false;
        vector<char> used(10, 0);
        while (it < 10500500) {
            i64 tmp = cur;
            while (tmp) {
                used[tmp % 10] = 1;
                tmp /= 10;
            }
            if (check(used)) {
                found = true;
                break;
            }
            cur = (it + 1) * n;
            it++;
        }
        if (found) {
            cout << "Case #" << k <<": " << cur << "\n";
        } else {
            cout << "Case #" << k <<": " << "INSOMNIA" << "\n";
        }
    }
    return 0;
}























