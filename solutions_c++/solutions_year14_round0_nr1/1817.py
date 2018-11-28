#include<stdio.h>
int ma[5][5],mb[5][5];
int ans;
int look(int *ra,int *rb)
{
    int num=0,i,j;
    for(i=1;i<=4;i++)
    for(j=1;j<=4;j++)
    if(ra[i]==rb[j]) {num++;ans=ra[i];}
    return num;

}
int main()
{
    int n,i,t,k1,k2,x,y,l;
    scanf("%d",&n);
    t=1;
    while(n--)
    {
        scanf("%d",&k1);
        for(x=1;x<=4;x++)
        for(y=1;y<=4;y++)
        scanf("%d",ma[x]+y);
        scanf("%d",&k2);
        for(x=1;x<=4;x++)
        for(y=1;y<=4;y++)
        scanf("%d",mb[x]+y);
        l=look(ma[k1],mb[k2]);
        if(l==1) printf("Case #%d: %d\n",t++,ans);
        else if(l>1) printf("Case #%d: Bad magician!\n",t++);
        else printf("Case #%d: Volunteer cheated!\n",t++);
    }

    return 0;
}
