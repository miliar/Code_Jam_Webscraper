#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PII;
int d,p[1001];
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d",&T);
    int ca = 0;
    while (T--) {
        scanf("%d",&d);
        int m = 0;
        for (int i = 0; i<d; i++) {
            scanf("%d",&p[i]);
            m = max(m,p[i]);
        }
        int ans = m,tmp;
        for (int i = 1; i<m; i++) {
            tmp = 0;
            for (int j = 0; j<d; j++)
                tmp += p[j]/i + (p[j]%i==0?0:1) - 1;
            ans = min(ans,tmp+i);
        }
        printf("Case #%d: %d\n",++ca,ans);
    }
}
