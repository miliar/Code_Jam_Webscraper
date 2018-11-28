#include<stdio.h>
#include<string.h>

int a[10][10],b[10][10];
int c[10];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,tt,i,j,n,m,num;
    scanf("%d",&t);
    tt = 0;
    while(t--){
        tt++;
        scanf("%d",&n);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&m);
        for(i = 1; i <= 4; i++)
            for(j = 1; j <= 4; j++)
                scanf("%d",&b[i][j]);
        num = 0;
        for(i = 1; i <= 4; i++){
            for(j = 1; j <= 4; j++){
                if(a[n][i]==b[m][j])
                    c[num++] = a[n][i];
            }
        }
        if(num==1)
            printf("Case #%d: %d\n",tt,c[0]);
        else if(num==0)
            printf("Case #%d: Volunteer cheated!\n",tt);
        else
            printf("Case #%d: Bad magician!\n",tt);
    }
    return 0;
}
