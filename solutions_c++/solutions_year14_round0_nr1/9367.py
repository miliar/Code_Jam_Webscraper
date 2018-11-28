#include<stdio.h>

int main(){
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);
    int i, j, n1, n2, a[5][5], b[5][5], T, ans=-2, abc;
    scanf("%d", &T);
    for(abc=0;abc<T;abc++){
        ans=-2;
        scanf("%d", &n1);n1--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d", &a[i][j]);
        scanf("%d", &n2);n2--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d", &b[i][j]);
        for(i=0;i<4 && ans != -1;i++){
            for(j=0;j<4;j++){
                if(a[n1][i] == b[n2][j]){
                    if(ans == -2)ans = a[n1][i];
                    else {
                        ans = -1;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: ", abc+1);
        if(ans == -1)printf("Bad magician!\n");
        else if(ans == -2)printf("Volunteer cheated!\n");
        else printf("%d\n",ans);
    }
}
