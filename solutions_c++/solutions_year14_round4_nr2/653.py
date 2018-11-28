#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <set>

using namespace std;
struct Point {
    int val, id;
} p[1010];

bool cmp0(const Point & A, const Point & B) {
    return A.id < B.id;
}
bool cmp1(const Point & A, const Point & B) {
    return A.val < B.val;
}
int rank[1010];
int Query(int who) {
    int ret = 0;
    for(int i = 1; i < who; i++) {
        if(p[i].val > p[who].val) {
            ret++;   
        }
    }
    return ret;
}
int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T = 0, Cas = 0;
    scanf("%d", &T);
    while(T--) {
        int n;
        scanf("%d",&n);
        for(int i = 1; i <= n; i++) {
            scanf("%d", &p[i].val);
            p[i].id = i;
        }
        sort(p + 1,p + 1 + n,cmp1);
        for(int i = 1; i <= n; i++) {
            rank[i] = p[i].id;
        }
        sort(p + 1, p + 1 + n, cmp0);
        int ans=0;
        for(int i = 1; i < n; i++) {
            int x = Query(rank[i]);
            int tmp = n - i - x;
            ans += min(x, tmp);
        }
        printf("Case #%d: %d\n",++Cas, ans);
    }
    return 0;
}
