#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
using namespace std;
#define f first
#define s second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <string, string> pss;
typedef vector <int> lint;
typedef long double db;
const db EPS = 1e-8;
db solve() {
    db c, f, x;
    cin >> c >> f >> x;
    if (x < c + EPS)
        return x / 2;
   int cnt = (int)(x + 10);
   db now = 2;
   db sumtm = 0;
   db ans = 1e9;
   for (int i = 0; i <= cnt; ++i) {
       ans = min(ans, sumtm + x / now);
       sumtm += c / now;
       now += f;
   }
   return ans;
}
         
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
        printf("Case #%d: %.8f\n", i + 1, (double)solve());
    return 0;
}
