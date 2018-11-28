#include <cstdio>
#include <unordered_map>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <cmath>
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

int t, k, c, s;

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for(int tc = 1; tc <= t; ++tc) {
        cin >> k >> c >> s;
        cout << "Case #" << tc << ":";
        for(int i = 0; i < k; ++i) {
            cout << " " << i + 1;
        }
        cout << endl;
    }
}
