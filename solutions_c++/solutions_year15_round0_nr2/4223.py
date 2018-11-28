#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
using namespace std;


#define INF 1e+9
#define mp make_pair
#define lint long long
#define pii pair<int, int>
#define MAXN 1100
#define MAXH 2010

int p[MAXN];

bool possible(int d, int splits, int t) {
    for (int i = 0; i < d; i++) {
        splits -= (p[i] - 1) / t;
    }
    return splits >= 0;
}


int main() {
    ios_base::sync_with_stdio(false);
    int t; 
    cin >> t;
    for (int ii = 0; ii < t; ii++) {
        int d; cin >> d;
        for (int i = 0; i < d; i++) {
            cin >> p[i];
        }
        int mint = INF;
        for (int splits = 0; splits < 2000; splits++) {
            int l = 0, r = 2000;
            while (l + 1 < r) {
                int m = (l + r + 1) / 2;
                if (possible(d, splits, m)) r = m;
                else l = m;
            }
            mint = min(mint, r + splits);
        }
        cout << "Case #" << ii+1 << ": " << mint << endl;
    }
}
