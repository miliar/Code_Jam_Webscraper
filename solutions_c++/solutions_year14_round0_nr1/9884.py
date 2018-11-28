#include<stdio.h>
int a1[5][5], a2[5][5];
int main(){
//
//    freopen("A-small-attempt4.in","r",stdin);
//    freopen("A4.out", "w", stdout);
    int n, m, p, i, j, sum, judge;
    scanf("%d", &n);
    for(int t = 1; t <= n; t++){
        scanf("%d",&m);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                scanf("%d", &a1[i][j]);
        scanf("%d", &p);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                scanf("%d", &a2[i][j]);
        sum = 0;
        printf("Case #%d: ", t);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                if(a1[m][i] == a2[p][j]){
                    sum++;
                    judge = a1[m][i];
                }
        if(sum == 0)
            printf("Volunteer cheated!\n");
        else if(sum == 1)
            printf("%d\n", judge);
        else
            printf("Bad magician!\n");
    }
    return 0;
}
