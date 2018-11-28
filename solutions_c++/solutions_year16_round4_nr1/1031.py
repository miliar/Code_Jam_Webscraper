#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iterator>
#include <utility>
#include <algorithm>
#include <list>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define pb push_back
#define sz(v) ((long long)v.size())
#define mp make_pair
#define FOR(i,n) for(long long i = 0;i < (n);++i)
#define MOD 1000000007

string check(int p, int r, int s) {
    if (p + r + s == 1) {
        if (p)
            return "P";
        if (r)
            return "R";
        if (s)
            return "S";
    }
    int c = (p + s - r) / 2;
    int a = p - c;
    int b = s - c;
    if (a < 0 || b < 0 || c < 0) {
        return "";
    }

    string res = check(a, b, c);
    if (res == "") return res;

    string res2;
    FOR(i, res.size()) {
        if (res[i] == 'P') {
            res2 += "PR";
        } else if (res[i] == 'R') {
            res2 += "RS";
        } else {
            res2 += "PS";
        }
    }
    return res2;
}

string mysort(string str) {
    if (str.size() == 1) {
        return str;
    }
    string str1(str.begin(), str.begin()+str.size()/2);
    string str2(str.begin()+str.size()/2, str.end());
    str1 = mysort(str1);
    str2 = mysort(str2);
    if (str1 > str2) {
        return str2 + str1;
    } else {
        return str1 + str2;
    }
}

int main() {
    int T;
    cin >> T;
    FOR(iter, T) {
        cout << "Case #" << iter + 1 << ": ";
        int n,r,p,s;
        cin >> n >> r >> p >> s;
        string res = check(p, r, s);
        if (res.size() > 0) {
            cout << mysort(res) << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }

    }
  
}