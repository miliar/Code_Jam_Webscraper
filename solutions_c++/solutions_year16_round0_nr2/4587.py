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

int rec(vector<char> &v, int pos) {
    int res = 0;
    int index = pos;
    for (; index >= 0; index--) {
        if (v[index] == 0) {
            break;
        }
    }
    if (index < 0 || (index == 0 && v[index] == 1)) {
        return res;
    }
    //swap all + from the left
    bool didSmth = false;
    for (int i = 0; i < index; i++) {
        if (v[i] == 0) {
            break;
        }
        didSmth = true;
        v[i] = 0;
    }
    if (didSmth) res++;
    //swap everythin from left to right group of +
    for (int i = 0; i <= index / 2; i++) {
        swap(v[i], v[index - i]);
        v[i] = 1 - v[i];
        if(i != index - i) v[index - i] = 1 - v[index - i];
    }
    res++;
    return res + rec(v, index);
}

int main(){
#ifndef _DEBUG
    /*freopen("strings.in", "r", stdin);
     freopen("strings.out", "w", stdout);*/
#endif
    freopen("/users/zakhar/documents/xcode projects/olymp/olymp/olymp/B-large.in", "r", stdin);
    freopen("/users/zakhar/documents/xcode projects/olymp/olymp/olymp/output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int t;
    string s;
    cin >> t;
    for (int k = 1; k <= t; k++) {
        cin >> s;
        vector<char> v(s.length());
        for (int i = 0; i < s.length(); i++) {
            v[i] = (s[i] == '+' ? 1 : 0);
        }
        cout << "Case #" << k << ": " << rec(v, (int)v.size() - 1) << "\n";
    }
    return 0;
}














