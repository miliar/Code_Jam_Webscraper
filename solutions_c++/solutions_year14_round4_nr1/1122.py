#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int maxn = 20000;

int T,N,X;
int S[maxn];

int main() {
    #ifndef ONLINE_JUDGE
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    #endif // ONLINE_JUDGE
    scanf("%d",&T);
    for (int kase = 1;kase <= T; kase++) {
        scanf("%d%d",&N,&X);
        for (int i = 1;i <= N; i++) scanf("%d",&S[i]);
        sort(S+1,S+N+1);
        int ed = 1,ans = 0;
        for (int i = N;i >= ed; i--) {
            if (S[i]+S[ed] <= X) ed++;
            ans++;
        }
        printf("Case #%d: %d\n",kase,ans);
    }
    return 0;
}
