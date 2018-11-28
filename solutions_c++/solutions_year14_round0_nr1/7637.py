#include <stdio.h>
int main() {
        int cas,ca = 0;
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
        scanf("%d",&cas);
        while (cas--) {
                bool vis[20] = {0};
                int n;
                scanf("%d",&n);
                for (int i = 0; i < 4; i ++) {
                        for (int j = 0; j < 4; j ++) {
                                int x;
                                scanf("%d",&x);
                                if (i==n-1) {
                                        vis[x] = 1;
                                }
                        }
                }
                scanf("%d",&n);
                for (int i = 0; i < 4; i ++) {
                        for (int j = 0; j < 4; j ++) {
                                int x;
                                scanf("%d",&x);
                                if (i!=n-1) {
                                        vis[x] = 0;
                                }
                        }
                }
                int cnt = 0,p = -1;
                for (int i = 1; i <= 16; i ++) {
                        if (vis[i]) cnt ++, p = i;
                }
                printf("Case #%d: ",++ca);
                if (cnt==0) {
                        puts("Volunteer cheated!");
                } else if (cnt!=1) {
                        puts("Bad magician!");
                } else {
                        printf("%d\n",p);
                }
        }
        return 0;
}
