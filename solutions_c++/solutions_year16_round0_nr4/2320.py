#include <bits/stdc++.h>
using namespace std;
int t,n,m,k;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d",&t);
    for (int i=0;i<t;i++) {
        scanf("%d %d %d",&n,&m,&k);
        printf("Case #%d: ",i+1);
        for (int j=1;j<=n;j++) {
            printf("%d%c",j,j==n?'\n':' ');
        }
    }
    return 0;
}
