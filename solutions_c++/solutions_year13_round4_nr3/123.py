#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std ;

const int MAXN = 20009 ;

#define PB push_back
#define MP make_pair
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fi(i,a,b) for(int i=a;i>=b;i--)
#define add(a,b) \
	do { \
		d[b] ++ ; \
		edge[a].PB(b) ; \
	} while(0)

int n , d[MAXN] , z[MAXN] , q[MAXN] , a[MAXN] , b[MAXN] , ans[MAXN] ;
vector<int> edge[MAXN] ;

void work() {
    int k = 0, tmp = 0;
    for (int i = 1; i <= n; ++i) if (d[i] == 0) z[++k] = i;
    for (int i = 1; i <= n; ++i) {
        for (int j = i; j <= k; ++j) if (z[j] < z[i]) swap(z[j], z[i]);
        ans[z[i]] = i;
        for (int j = 0; j < edge[z[i]].size(); ++j) {
            --d[tmp = edge[z[i]][j]];
            if (d[tmp] == 0) z[++k] = tmp;
        }
    }
}

void Init() {
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i){
        ans[i] = 0;
        edge[i].clear();
    }
    for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
    for (int i = 1; i <= n; ++i) scanf("%d", &b[i]);
}

void Solve() {
    for (int i = 1; i <= n; ++i) q[i] = 0;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= a[i] - 1; ++j) if (q[j] != 0) add(q[j], i);
        for (int j = a[i]    ; j <= n; ++j) if (q[j] != 0) add(i, q[j]);
        q[a[i]] = i;
    }
    for (int i = 1; i <= n; ++i) q[i] = 0;
    for (int i = n; i > 0; --i) {
        for (int j = 1; j <= b[i] - 1; ++j) if (q[j]) add(q[j], i);
        for (int j = b[i];     j <= n; ++j) if (q[j]) add(i, q[j]);
        q[b[i]] = i;
    }
    work();
    for (int i = 1; i <= n; ++i) {
        int m = 1;
        for (int j = 1; j <= i - 1; ++j)
        if (ans[i] > ans[j]) m = max(m, a[j] + 1);
    }
    for (int i = n; i > 0; --i) {
        int m = 1;
        for (int j = n; j > i; --j)
        if (ans[j] < ans[i]) m = max(m, b[j] + 1);
    }
}

int main(){
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int Test ; scanf("%d", &Test);
    for (int t = 1; t <= Test; ++t) {
	Init() ;
	Solve() ;
        printf("Case #%d:", t);
        for (int i = 1; i <= n; ++i) printf(" %d", ans[i]);
        printf("\n");
    }
}


