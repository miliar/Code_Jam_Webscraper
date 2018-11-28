#include <stdio.h>

int main(void)
{
    int tn, n, i, j, k, x;
    int ans, count, r1, r2;
    int test[4];
    scanf("%d", &tn);
    for(n=1;n<=tn;n++){
        printf("Case #%d: ",n);
        scanf("%d", &r1);
        r1--;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                scanf("%d", &x);
                if(i==r1){
                    test[j]=x;
                }
            }
        }
        scanf("%d", &r2);
        r2--;
        count=0;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                scanf("%d", &x);
                if(i==r2){
                    for(k=0;k<4;k++){
                        if(x==test[k]){
                            ans = x;
                            count++;
                        }
                    }
                }
            }
        }
        if(count==0)
            printf("Volunteer cheated!\n");
        else if(count==1)
            printf("%d\n", ans);
        else
            printf("Bad magician!\n");
    }

    return 0;
}
