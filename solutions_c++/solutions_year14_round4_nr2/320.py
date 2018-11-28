#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int a[1010];
bool vis[1010];
vector<pair<int, int> > p;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t, n;
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ca ++ ) {
        scanf("%d", &n);
        p.clear();
        for (int i = 0; i < n; i ++ ) {
            scanf("%d", &a[i]);
            p.push_back(make_pair(a[i], i));
        }
        int cnt = 0;
        sort(p.begin(), p.end());
        memset(vis, 0, sizeof(vis));
        for (int i = 0; i < n; i ++ ) {
            int se = p[i].second, ct1 = 0, ct2 = 0;
            vis[se] = true;
            for (int j = 0; j < n; j ++ )
                if (!vis[j]) {
                    if (j < se) ct1 ++ ;
                    else ct2 ++ ;
                }
            //cout<<se<<" "<<ct1<<" "<<ct2<<endl;
            cnt += min(ct1, ct2);
        }
        printf("Case #%d: %d\n", ca, cnt);
    }
    return 0;
}

