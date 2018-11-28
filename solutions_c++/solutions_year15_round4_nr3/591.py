#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <set>
 
#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)
 
typedef long long int64;
 
using namespace std;

int64 p = 43;

int64 hash(string s) {
    int64 result = 0;
    int64 deg = 1;
    for (int i = 0; i < sz(s); ++i) {
        result += (s[i] - 'a' + 1) * deg;
        deg *= p;
    }
    return result * 10 + sz(s) - 1;
}

vector<int64> split(string s) {
    vector<int64> res;
    string str;
    s.pb(' ');
    for (int i = 0; i < sz(s); ++i) {
        if (s[i] == ' ') {
            if (!str.empty()) res.pb(hash(str));
            str.clear();
            continue;
        } 
        str.pb(s[i]);
    }
    return res;
}

void solve() {
   int n;
   cin >> n;
   string s;
   getline(cin, s);
   vector<vector<int64> > words;
   for (int i = 0; i < n; ++i) {
      getline(cin, s);
      words.pb(split(s));
   }
   set<int64> _a1;
   set<int64> _a2;
   for (int j = 0; j < sz(words[0]); ++j) _a1.insert(words[0][j]);
   for (int j = 0; j < sz(words[1]); ++j) _a2.insert(words[1][j]);
   int cnt = 0;
   for (set<int64>::iterator it = _a1.begin(); it != _a1.end(); ++it)
           if (_a2.find(*it) != _a2.end())
               ++cnt;
   int ans = 1000000000;
   for (int i = 0; i < (1 << (n - 2)); ++i) {
       set<int64> a1;
       set<int64> a2;
       int res = cnt;
       for (int j = 0; j < n - 2; ++j) {
           if (i & (1 << j)) {
               for (int k = 0; k < sz(words[j + 2]); ++k) {
                   int64 val = words[j + 2][k];
                   if (_a1.find(val) == _a1.end() && a1.find(val) == a1.end()) {
                       a1.insert(val);
                       if (_a2.find(val) != _a2.end()) {
                           ++res;
                       }
                   }
               }
           }
       }
       for (int j = 0; j < n - 2; ++j) {
           if (!(i & (1 << j))) {
               for (int k = 0; k < sz(words[j + 2]); ++k) {
                   int64 val = words[j + 2][k]; 
                   if (_a2.find(val) == _a2.end() && a2.find(val) == a2.end())
                       if (a1.find(val) != a1.end() || _a1.find(val) != _a1.end())
                           ++res;
                   a2.insert(val);
               }
           }
       }
       ans = min(ans, res);
   }
   cout << ans << endl;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
