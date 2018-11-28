#include<cstdio>
using namespace std;
int i,j,k,l,m,n,a,b,z=0,ar[100],t,c,d,cnt;
int main()
{
    freopen("m.in","r",stdin);
    freopen("k.out","w",stdout);
scanf("%d",&t);
while(t--)
{   z++;
cnt=0;
scanf("%d",&n);
for(i=1;i<=4;i++)
{
    scanf("%d %d %d %d",&a,&b,&c,&d);
    if(i==n)
    {   //printf("\n");
        //printf("\n%d %d %d %d\n",a,b,c,d);
        ar[a]++;ar[b]++;
        ar[c]++;ar[d]++;

    }
}
scanf("%d",&n);
for(i=1;i<=4;i++)
{
    scanf("%d %d %d %d",&a,&b,&c,&d);
    if(i==n)
    {  // printf("\n");
        //printf("%d %d %d %d\n",a,b,c,d);
        ar[a]++;ar[b]++;
        ar[c]++;ar[d]++;

    }
}
for(i=0;i<=16;i++)
{
    if(ar[i]==2)
    cnt++,j=i;
   // printf("%d %d\n",i,ar[i]);

    ar[i]=0;

}
if(cnt==1)
printf("Case #%d: %d\n",z,j);
else
if(cnt==0)
printf("Case #%d: Volunteer cheated!\n",z);
else
printf("Case #%d: Bad magician!\n",z);





}
return 0;
}
