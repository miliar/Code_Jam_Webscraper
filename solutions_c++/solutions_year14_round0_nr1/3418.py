#include<cstdio>
#include<cmath>
int main()
{
    int t,a,b,n[4][4],m[4][4],i,j;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    for(int cnt = 1;cnt<=t;cnt++){
        scanf("%d",&a);
        for(i=0;i<4;i++)for(j=0;j<4;j++)
            scanf("%d",&n[i][j]);
        scanf("%d",&b);
        for(i=0;i<4;i++)for(j=0;j<4;j++)
            scanf("%d",&m[i][j]);
        a--;b--;
        int same = -1, sn = 0;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(n[a][i] == m[b][j]){
                    sn++;
                    same = n[a][i];
                }
            }
        }
        printf("Case #%d: ",cnt);
        if(sn == 0){
            printf("Volunteer cheated!\n");
        }else if(sn == 1){
            printf("%d\n",same);
        }else{
            printf("Bad magician!\n");
        }

    }
    return 0;
}
