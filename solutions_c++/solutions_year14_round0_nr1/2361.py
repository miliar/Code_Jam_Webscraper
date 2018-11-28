#include <cstring>
#include <cstdio>
const int N = 20;
int T,C,k,n,x,h[N],ans[N];
int main() {
    scanf("%d",&T);
    for (int C = 1;C <= T;C++) {
        memset(h,0,sizeof(h));
        memset(ans,0,sizeof(ans));
        scanf("%d",&k);
        for (int i = 1;i <= 4;i++)
            for (int j = 1;j <= 4;j++) {
                scanf("%d",&x);
                if (i == k) h[x]++;
            }
        scanf("%d",&k);
        for (int i = 1;i <= 4;i++)
            for (int j = 1;j <= 4;j++) {
                scanf("%d",&x);
                if (i == k) h[x]++;
            }
        int s = 0;
        for (int i = 1;i <= 16;i++)
            if (h[i] == 2) ans[s++] = i;
        printf("Case #%d: ",C);
        if (s == 1) printf("%d\n",ans[0]);
        else if (s == 0) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    return 0;
}
