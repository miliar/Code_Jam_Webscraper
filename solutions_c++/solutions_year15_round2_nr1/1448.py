#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <bitset>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)
#define pb push_back
#define mp make_pair
#define EPS 1.0e-8
#define INF 1000000000

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;

int dist[1000005];

int digitReverse(int x) {
    int ret = 0;
    while(x) {
        ret *= 10;
        ret += x%10;
        x /= 10;
    }
    return ret;
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int T;
    int n, u, v;

    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%d", &n);
        queue<int> q;
        memset(dist, -1, sizeof(dist));
        q.push(1); dist[1] = 1;
        while(dist[n] == -1) {
            u = q.front(); q.pop();

            v = u+1;
            if (dist[v] == -1 && v<=n) {
                dist[v] = dist[u]+1;
                q.push(v);
            }

            v = digitReverse(u);
            if (dist[v] == -1 && v<=n) {
                dist[v] = dist[u]+1;
                q.push(v);
            }
        }

        printf("Case #%d: %d\n", ncase, dist[n]);
    }

    return 0;
}
