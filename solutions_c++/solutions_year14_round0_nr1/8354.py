#include <cstdio>
#include <cstring>
int main() {
        int T,ca=1;
        freopen("A-small-attempt1.in","r",stdin);
        freopen("A.out","w",stdout);
        scanf("%d",&T);
        while(T--) {
                int a[4][4], b[4][4];
                int r1, r2;
                scanf("%d",&r1);
                for(int i = 0; i < 4; i++) {
                        for(int j = 0; j < 4; j++) {
                                scanf("%d",&a[i][j]);
                        }
                }
                scanf("%d",&r2);
                for(int i = 0; i < 4; i++) {
                        for(int j = 0; j < 4; j++) {
                                scanf("%d",&b[i][j]);
                        }
                }
                r1--;r2--;
                int cnt = 0;
                int num, ans;
                for(int i = 0; i < 4; i++) {
                        num = a[r1][i];
                        for(int j = 0; j < 4; j++) {
                                if(num == b[r2][j]) {
                                        ans = num;
                                        cnt++;
                                        break;
                                }
                        }
                }
                printf("Case #%d: ",ca++);
                if(cnt == 1) {
                        printf("%d\n",ans);
                } else if(cnt == 0) {
                        puts("Volunteer cheated!");
                } else {
                        puts("Bad magician!");
                }
        }
        return 0;
}
