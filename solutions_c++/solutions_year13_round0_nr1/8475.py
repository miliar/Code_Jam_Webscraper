#include<cstdio>
char table[5][5];
int main(){
    int n,i,j,k;
    int ans;
    int counto,countx,countt,countother;
    freopen("output.txt","w",stdout);
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        countother=0;
        for(j=1;j<=4;j++){
            for(k=1;k<=4;k++){
                scanf(" %c",&table[j][k]);
            }
        }
        ans=1;
        for(j=1;j<=4&&ans==1;j++){
            counto=0;
            countx=0;
            countt=0;
            for(k=1;k<=4;k++){
                if(table[j][k]=='O')    counto++;
                if(table[j][k]=='X')    countx++;
                if(table[j][k]=='T')    countt++;
                if(table[j][k]=='.')    countother++;
            }
            if(counto+countt==4){
                printf("Case #%d: O won",i);
                ans=0;
            }
            if(countx+countt==4){
                printf("Case #%d: X won",i);
                ans=0;
            }
        }
        for(j=1;j<=4&&ans==1;j++){
            counto=0;
            countx=0;
            countt=0;
            for(k=1;k<=4;k++){
                if(table[k][j]=='O')    counto++;
                if(table[k][j]=='X')    countx++;
                if(table[k][j]=='T')    countt++;
            }
            if(counto+countt==4){
                printf("Case #%d: O won",i);
                ans=0;
            }
            if(countx+countt==4){
                printf("Case #%d: X won",i);
                ans=0;
            }
        }
        if(ans==1){
            counto=0;
            countt=0;
            countx=0;
            for(j=1;j<=4;j++){
                if(table[j][j]=='O')    counto++;
                if(table[j][j]=='X')    countx++;
                if(table[j][j]=='T')    countt++;
            }
            if(counto+countt==4){
                printf("Case #%d: O won",i);
                ans=0;
            }
            if(countx+countt==4){
                printf("Case #%d: X won",i);
                ans=0;
            }
        }
        if(ans==1){
            counto=0;
            countt=0;
            countx=0;
            for(j=1;j<=4;j++){
                if(table[j][5-j]=='O')  counto++;
                if(table[j][5-j]=='X')  countx++;
                if(table[j][5-j]=='T')  countt++;
            }
            if(counto+countt==4){
                printf("Case #%d: O won",i);
                ans=0;
            }
            if(countx+countt==4){
                printf("Case #%d: X won",i);
                ans=0;
            }
        }
        if(ans==1&&countother!=0)   printf("Case #%d: Game has not completed",i);
        if(ans==1&&countother==0)   printf("Case #%d: Draw",i);
        if(i!=n)                    printf("\n");
    }
    return 0;
}
