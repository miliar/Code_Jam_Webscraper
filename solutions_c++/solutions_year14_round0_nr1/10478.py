#include<stdio.h>
#include<stdlib.h>

int main(){
    FILE *fp;
    int ar1[5],ar2[5];
    int a,b,c=1,d,n,i,j,t,temp,g;
    freopen("A-small-attempt0.in","r",stdin);
    fp = fopen("ans.txt", "w");
    scanf("%d",&t);
    while(t--){
        d=0;
        scanf("%d",&a);
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                if(i==a)
                    scanf("%d",&ar1[j]);
                else
                    scanf("%d",&g);
            }
        }
        scanf("%d",&a);
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                if(i==a)
                    scanf("%d",&ar2[j]);
                else
                    scanf("%d",&g);
            }
        }
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                if(ar1[i]==ar2[j]){
                    d++;
                    temp=ar1[i];
                }
            }
        }
        fprintf(fp, "Case #%d: ",c++);
        if(d==1){
            fprintf(fp, "%d\n",temp);
        }
        else if(d==0){
            fprintf(fp, "Volunteer cheated!\n");
        }
        else{
            fprintf(fp, "Bad magician!\n");
        }
    }
    fclose(fp);
    return 0;
}
