#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <cassert>
#include <vector>
#include <set>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

#define ll long long
#define point pair<double, double>
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define uint unsigned int
#define merge botva
#define M_PI 3.14159265358979323846
#define left b1
#define right b2

#define plus botva12


const int INF = 1200000000, mod = 1000002013, maxn = 1006;

int dx[] = {-1, 0, 1,  0};
int dy[] = { 0, 1, 0, -1};


long double dp[1 << 21];

int main() {
        int t, af;
        cin >> t;
        string s;
        for (int zi = 0; zi < t; ++zi) {
                cin >> s;
                int init = 0;
                for (int i = 0; i < s.size(); ++i)
                        if (s[i] == 'X') init += (1 << i);
                int n = s.size();
                memset(dp, 0, sizeof dp);
                for (int i = (1 << n) - 2; i >= 0; --i) {
                        for (int j = 0; j < n; ++j) {
                                int k = j, prev = n;
                                while ((1 << k) & i) {
                                        --prev;
                                        k = (k + 1) % n;
                                }
                                dp[i] += (dp[(1 << k) | i] + prev) / n;
                        }
                }
                printf("Case #%d: ", zi + 1);
                cout.precision(20);
                cout << dp[init] << endl;
        }
}
