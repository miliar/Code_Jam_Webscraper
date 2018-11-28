#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <vector>
#include <string>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef pair<int,int> PII;
#define MP make_pair
#define PB push_back
#define A first
#define B second
#define eps 1e-8
#define mod 1000002013
struct node {
    LL x, p;
    int f;
} w[2010];

int t, m;
LL n;

bool cmp(const node &x, const node &y) {
    return x.x == y.x ? x.f < y.f : x.x < y.x;
}

LL q[2010][2];

LL work(LL p, LL L) {
    return (n * 2 - L + 1) * L / 2 % mod * p % mod;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ca ++ ) {
        cin>>n>>m;
        LL ans1 = 0;
        for (int i = 0; i < m; i ++ ) {
            int o, e, p;
            scanf("%d%d%d", &o, &e, &p);
            ans1 = (ans1 + work(p, e - o)) % mod;
            w[i].x = o, w[i].p = p, w[i].f = 1;
            w[i + m].x = e, w[i + m].p = p, w[i + m].f = 2;
        }
        sort(w, w + m * 2, cmp);
        int top = 0;
        LL ans = 0;
        for (int i = 0; i < m * 2; i ++ ) {
            //cout<<w[i].x<<"--"<<w[i].f<<endl;
            if (w[i].f == 1) {
                q[top][0] = w[i].x;
                q[top][1] = w[i].p;
                top ++ ;
            }
            else {
                LL p = w[i].p, r = w[i].x, l;
                while (p) {
                    top -- ;
                    l = q[top][0];
                    LL p1 = q[top][1], mp;
                    mp = min(p, p1);
                    ans = (ans + work(mp, r - l)) % mod;
                    p -= mp;
                    p1 -= mp;
                    if (p1) {
                        q[top][1] = p1;
                        top ++ ;
                    }
                }
            }
        }
        ans = (ans1 - ans + mod) % mod;
        printf("Case #%d: %I64d\n", ca, ans);
    }
    return 0;
}
