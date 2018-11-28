#include<stdio.h>
int a[4],T,x,y;

int main() {
    freopen("input.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        printf("Case #%d: ",t);
        scanf("%d",&x);
        for(int i=0;i<4;++i) {
            for(int j=0;j<4;++j) {
                scanf("%d",&y);
                if(i==x-1) {
                    a[j]=y;
                }
            }
        }
        scanf("%d",&x);
        int ret = 0;
        for(int i=0;i<4;++i) {
            for(int j=0;j<4;++j) {
                scanf("%d",&y);
                if(i==x-1) {
                    for(int k=0;k<4;++k) {
                        if(a[k]==y) {
                            if(ret) {
                                ret = 17;
                            } else {
                                ret = y;
                            }
                        }
                    }
                }
            }
        }
        if(ret==0) {
            printf("Volunteer cheated!\n");
        } else if(ret==17) {
            printf("Bad magician!\n");
        } else {
            printf("%d\n",ret);
        }
    }
    return 0;
}
