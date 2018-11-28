#include <stdio.h>

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,t;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int chk[20]={0};
        int cnt[5]={0};
        int a[5][5];
        int i,j,n;
        scanf("%d",&n);
        n--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        }
        for(i=0;i<4;i++) chk[a[n][i]]++;
        scanf("%d",&n);
        n--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        }
        for(i=0;i<4;i++) chk[a[n][i]]++;
        for(i=1;i<=16;i++) cnt[chk[i]]++;
        if(cnt[2]>1) printf("Bad magician!\n");
        else if(cnt[2]==0) printf("Volunteer cheated!\n");
        else
        {
            for(i=1;i<=16;i++)
                if(chk[i]==2) printf("%d\n",i);
        }
    }
}
