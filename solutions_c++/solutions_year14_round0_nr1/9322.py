#include <stdio.h>
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,b[4][4],r1,r2,a[4][4],count,p;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        count=0;
        scanf("%d",&r1);
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                scanf("%d",&a[j][k]);
            }
        }
        scanf("%d",&r2);
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                scanf("%d",&b[j][k]);
            }
        }
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                if(a[r1-1][j]==b[r2-1][k]){
                    count++;
                    p=a[r1-1][j];
                }
            }
        }
        if(count<1) printf("Case #%d: Volunteer cheated!\n",i+1);
        else if(count>1)    printf("Case #%d: Bad magician!\n",i+1);
        else    printf("Case #%d: %d\n",i+1,p);
    }
    return 0;
}
