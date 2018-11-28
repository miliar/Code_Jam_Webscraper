#include<stdio.h>
main()
{
    int t,a,b,i,j,m[4][4],k[4][4],p,x,ans;
    scanf("%d",&t);
    for(x=1;x<=t;x++)
    {
        scanf("%d",&a);a--;p=0;
        for(i=0;i<4;i++) for(j=0;j<4;j++) scanf("%d",&m[i][j]);
        scanf("%d",&b);b--;
        for(i=0;i<4;i++) for(j=0;j<4;j++) scanf("%d",&k[i][j]);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            if(m[a][i]==k[b][j]) {p++;ans=m[a][i];}
        if(p==0) printf("Case #%d: Volunteer cheated!\n",x);
        else if(p==1) printf("Case #%d: %d\n",x,ans);
        else printf("Case #%d: Bad magician!\n",x);
    }
    return 0;
}
