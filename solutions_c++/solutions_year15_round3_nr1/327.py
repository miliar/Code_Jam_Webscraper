#include<bits/stdc++.h>
#define sc scanf
#define pr printf
#define fr first
#define se second
#define pb push_back
#define mp make_pair
using namespace std;
const int MN = 3010;
const int INF = (1LL<<32) - 1LL;
const int MOD = (1e+9) + 7;
const double eps = 1e-6;
int t, r, c, w;
int main(){
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    //freon("movetofront.in", "r", stdin); freopen("movetofront.out", "w", stdout
    sc("%d", &t);
    for (int k = 1; k <= t; k++) {
        pr ("Case #%d: ", k);
        sc("%d%d%d", &r, &c, &w);
        int ans = c / w * r - 1 + w;
        if (c % w != 0) {
            ans++;
        }
        pr("%d\n",  ans);
    }
    return 0;
}

