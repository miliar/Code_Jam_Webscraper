#include <stdio.h>
int main()
{
    //freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
    int t,te;
    scanf("%d",&t);
    for(te=1;te<=t;te++)
    {
        int rowa,rowb,a[4][4],b[4][4],i,j,th=-1;
        scanf("%d",&rowa);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)scanf("%d",&a[i][j]);
        scanf("%d",&rowb);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)scanf("%d",&b[i][j]);
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)if(a[rowa-1][i]==b[rowb-1][j]){if(th==-1)th=a[rowa-1][i];else th=-2;}
        if(th==-1)printf("Case #%d: Volunteer cheated!\n",te);
        else if(th==-2)printf("Case #%d: Bad magician!\n",te);
        else printf("Case #%d: %d\n",te,th);
    }
    return 0;
}
