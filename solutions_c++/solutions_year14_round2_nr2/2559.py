#include<cstdio>
#include<cstring>
int res[1005];
int main()
{
   // freopen("B-small-attempt0(1).in","r",stdin);
   // freopen("B_out.txt","w",stdout);
    int i,j,tamp,t,co=0,no,a,b,k;
    scanf("%d",&t);
    while(t--)
    {
        no=0;
        scanf("%d %d %d",&a,&b,&k);
    for(i=0;i<a;i++)
    for(j=0;j<b;j++)
    {
      tamp=i&j;
      if(tamp<k) no++;

    }
    printf("Case #%d: %d\n",++co,no);
    }
    return 0;
}
