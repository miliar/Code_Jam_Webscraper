#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <cstdio>
#include <cstring>
using namespace std;
#define ll long long
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define VI vector<int>
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
#define inf 1000000000
#define pdd pair<double, double>

int t;
int a[111];
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(int tc = 1; tc <= t; ++tc) {
        string s; cin >> s;
        int gr = 1, ans = 0;
        for(int i = 1; i < L(s); ++i) if (s[i] != s[i - 1]) ++gr;
        cout << "Case #" << tc << ": ";
        if (s[0] == '+') {
            cout << (gr / 2) * 2 << endl;
        } else {
            cout << ((gr - 1) / 2) * 2 + 1 << endl;
        }
    }
}

