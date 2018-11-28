#include<stdio.h>
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    char a[5][5],b[5][5];
    int count,n,m,T,t=0,i,j,ans;
    scanf("%d",&T);
    while(T--)
    {
        t++;
        scanf("%d",&n);
        for(i=0;i<4;i++)for(j=0;j<4;j++)
        scanf("%d",&a[i][j]);
        scanf("%d",&m);
        for(i=0;i<4;i++)for(j=0;j<4;j++)
        scanf("%d",&b[i][j]);
        count=0;
        for(i=0;i<4;i++) for(j=0;j<4;j++)
        if(a[n-1][i]==b[m-1][j]){count++; ans=a[n-1][i];}
        
        if(count==0) printf("Case #%d: Volunteer cheated!\n",t);
        else if(count>1) printf("Case #%d: Bad magician!\n",t);
        else printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
