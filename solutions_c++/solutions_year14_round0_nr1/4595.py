#include<cstdio>
using namespace std;
int i,j,pt,T,l,aij,ap[20];
int main()
{
//freopen("input","r",stdin);
//freopen("output","w",stdout);
scanf("%d",&T);
while(T)
{
    pt++;
    T--;
    for(i=1;i<=16;i++)
        ap[i]=0;
    scanf("%d",&l);
    for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        {
            scanf("%d",&aij);
            if(i==l) ap[aij]++;
        }
    scanf("%d",&l);
    for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        {
            scanf("%d",&aij);
            if(i==l) ap[aij]++;
        }
    for(i=1;i<=16;i++)
        if(ap[i]==2) break;
    printf("Case #%d: ",pt);
    if(i>16)
    {
        printf("Volunteer cheated!\n");
        continue;
    }
    for(j=i+1;j<=16;j++)
        if(ap[j]==2) break;
    if(j<=16)
    {
        printf("Bad magician!\n");
        continue;
    }
    printf("%d\n",i);
}
return 0;
}
