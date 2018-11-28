#include <stdio.h>
int a[5][5];
int b[5];
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n, m, j, l, i, k;
    scanf("%d", &n);
    for(i=1 ; i<=n ; i++){
        scanf("%d", &m);
        for(j=1 ; j<=4 ; j++){
            for(l=1 ; l<=4 ; l++){
                scanf("%d", &k);
                if(j==m)b[l]=k;
            }
        }
        scanf("%d", &m);
        int gap=0, dap=0;
        for(j=1 ; j<=4 ; j++){
            for(l=1 ; l<=4 ; l++){
                scanf("%d", &k);
                if(j==m){
                    int lk;
                    for(lk=1 ; lk<=4 ; lk++){
                        if(b[lk]==k){
                            gap++;
                            dap=k;
                        }
                    }
                }
            }
        }
        if(gap==0)printf("Case #%d: Volunteer cheated!", i);
        else if(gap==1)printf("Case #%d: %d", i, dap);
        else printf("Case #%d: Bad magician!", i);
        printf("\n");
    }
    return 0;
}
