#include <bits/stdc++.h>
using namespace std;

const int N=1e3+10;
int a[N], dp[N][N];

int main() {
    int n, t, T=1;
    for(int i=1; i<N; i++) for(int j=i; j>=1; j--) dp[i][(i+j-1)/j]=j-1;
    for(int i=1; i<N; i++) for(int j=1; j<i; j++) if(!dp[i][j]) dp[i][j]=dp[i][j-1];
    scanf("%d", &t);
    while(t--) {
        int ans=2e9;
        scanf("%d", &n);
        for(int i=0; i<n; i++) scanf("%d", &a[i]);
        for(int i=1; i<N; i++) {
            int sum=0;
            for(int j=0; j<n; j++) sum+=dp[a[j]][i];
            ans=min(ans, i+sum);
        }
        printf("Case #%d: %d\n", T++, ans);
    }
    return 0;
}
