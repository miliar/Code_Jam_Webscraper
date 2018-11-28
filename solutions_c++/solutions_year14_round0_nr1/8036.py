# include <stdio.h>
int main ()
{   freopen("A-small-attempt1.in","r",stdin);
    freopen("ans2.in","w",stdout);
    int t,a[5][5],p,b[5][5],q,count,ans;
    scanf("%d",&t);                                       
    for(int k=1;k<=t;k++)
{   scanf("%d",&p);
    for(int i=1;i<5;i++)
    for(int j=1;j<5;j++)
    scanf("%d",&a[i][j]);
    scanf("%d",&q);
    for(int i=1;i<5;i++)
    for(int j=1;j<5;j++)
    scanf("%d",&b[i][j]);
    count=0;
    for(int i=1;i<5;i++)
    for(int j=1;j<5;j++)
    if(a[p][i]==b[q][j]){count++;ans=a[p][i];}
    //printf("%d",count);  
    if(count==1)printf("Case #%d: %d\n",k,ans);
    if(count>1)printf("Case #%d: Bad magician!\n",k);
    if(count==0)printf("Case #%d: Volunteer cheated!\n",k);
}   //fclose();
    return 0;
}
