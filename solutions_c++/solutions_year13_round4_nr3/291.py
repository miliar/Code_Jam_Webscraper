#include<stdio.h>
#include<string.h>
#include<math.h>
#include<queue>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 2100
vector<int> e[maxn];
int tag[maxn];
int f[maxn], A[maxn], B[maxn], nb[maxn];
vector<int> vet[maxn];
int N;

int check() {
    int i, j;
    for (i = N - 1; i >= 0; i--) {
        f[i] = 1;
        for (j = i + 1; j < N; j++)
            if (nb[j] < nb[i])
                f[i] = max(f[j] + 1,f[i]);
        if ( B[i]!=f[i]) return 0;
    }
    return 1;

}

int dfs(int now) {
    if (now == N) {
        if (check()) return 1;
        else return 0;
    }
    int i, low, high;
    if (nb[now] != -1) return dfs(now + 1);
    else {
        high = N;
        for (i = 0; i < vet[A[now]].size(); i++)
            if (vet[A[now]][i] < now)
                high = min(high, nb[vet[A[now]][i]] - 1);
            else break;
        low = N;
        if (A[now] == 1) low = 1;
        else
            for (i = 0; i < vet[A[now] - 1].size() && vet[A[now] - 1][i] < now; i++)
                low = min(low, nb[vet[A[now] - 1][i]] + 1);
        for (i = low; i <= high; i++)if (!tag[i]) {
                nb[now] = i;
                tag[i] = 1;
                if (dfs(now + 1)) return 1;
                nb[now] = -1;
                tag[i] = 0;
            }


    }
    return 0;
}

int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
    int i, j, k, tt, cas;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas++) {
        scanf("%d", &N);
        for (i = 0; i < N; i++)
            scanf("%d", &A[i]);
        for (i = 0; i < N; i++)
            scanf("%d", &B[i]);
        for (i = 0; i < N; i++) vet[i].clear();
        for (i = 0; i < N; i++) vet[A[i]].push_back(i);
        memset(nb, -1, sizeof (nb));
        memset(tag, 0, sizeof (tag));

        int t = vet[1].size();
        for (i = 0; i < t; i++)
            nb[vet[1][i]] = t - i, tag[t - i] = 1;

        printf("Case #%d:", cas);
        memset(nb, -1, sizeof (nb));
        memset(tag, 0, sizeof (tag));
        if (dfs(0)) {
            for (i = 0; i < N; i++)
                printf(" %d", nb[i]);

        } else {
            nb[vet[1][t - 1]] = 1, tag[1] = 1;
            if (dfs(0)) {
                for (i = 0; i < N; i++)
                    printf(" %d", nb[i]);
            }
        }

        printf("\n");
    }
    return 0;
}
