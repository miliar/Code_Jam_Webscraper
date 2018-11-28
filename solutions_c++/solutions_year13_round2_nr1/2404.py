#define _USE_MATH_DEFINES

#include <vector>
#include <functional>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

vector<int> m;
vector<bool> del;
int gans, a, n;

void rec(int d, int s, int ans) {
    while (d < n && s > m[d]) {
        s += m[d];
        d++;
    }

    if (d == n) {
        gans = min(gans, ans);
        return;
    }

    rec(d + 1, s, ans + 1);

    if (s == 1) return;

    int tmp = s, k = 0;
    while (tmp <= m[d]) {
        tmp += tmp - 1;
        k++;
    }

    rec(d + 1, tmp + m[d], ans + k);

}

pair<int, int> d[1000000];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;

    for (int h = 1; h <= t; h++) {
        cin >> a >> n;
        gans = 1000000000;
        
        m.resize(n);
        for(int i = 0; i < n; i++)
            cin >> m[i];

        sort(m.begin(), m.end());

        rec(0, a, 0);
        /*int i = 1, s = a, ans;
        while(i <= n) {
            while (i <= n && s > m[i - 1]) {
                d[i].second = d[i - 1].second + m[i - 1];
                i++;
            }

            if (d[i].first > d[i - 1].first + 1) {
                d[i].first = d[i - 1].first + 1;
                d[i].second = d[i].second;
            }            

            if (s == 1) return;

            int tmp = d[i - 1].second, k = 0;
            while (tmp <= m[i - 1]) {
                tmp += tmp - 1;
                k++;
            }

            if (d[i].first > d[i - 1].first + k) {
                d[i].first = d[i - 1].first + k;
                d[i].second = tmp;
            }
        }*/

        cout << "Case #" << h << ": " << gans << endl;
    }
}
