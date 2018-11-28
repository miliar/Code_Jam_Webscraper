#include <stdio.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <ctime>
#include <cassert>
#include <unordered_map>
#include <fstream>
#include <random>
#include <cstring>
#include <complex>
#include <bitset>

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define pb push_back

using namespace std;

typedef long long ll;
typedef long double ld;
mt19937 rr(random_device{}());

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int q;
    cin >> q;
    for (int i = 0; i < q; ++i) {
        cout << "Case #" << i + 1 << ": ";
        string s;
        cin >> s;
        int k;
        cin >> k;
        int n = sz(s);
        bool f = true;
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '-') {
                if (n < k + i) {
                    f = false;
                    break;
                }
                ++cnt;
                for (int j = 0; j < k; ++j) {
                    s[i + j] = (s[i + j] == '-' ? '+' : '-');
                    
                }
            }
        }
        if (f) {
            cout << cnt << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
        
}
