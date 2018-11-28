#include<stdio.h>
int main()
{
int t,n,flag,a[4][4],b[4],c[4],i,j,l,ans,z;
scanf("%d",&t);
z=1;
while(t--)
{
flag=0;
    scanf("%d",&l);
    for(i=0;i<4;++i)
    {
        for(j=0;j<4;++j)
        {
        scanf("%d",&a[i][j]);
        if((i+1)==l)
        b[j]=a[i][j];
        }
    }

    scanf("%d",&l);
    for(i=0;i<4;++i)
    {
        for(j=0;j<4;++j)
        {
        scanf("%d",&a[i][j]);
        if((i+1)==l)
        c[j]=a[i][j];
        }
    }


for(i=0;i<4;++i)
{
for(j=0;j<4;++j)
{
//printf("%d %d\n",b[i],c[j]);
if(b[i]==c[j]){
flag++;
ans = b[i];}
}
}

if(flag==1)
{
printf("Case #%d: %d\n",z,ans);
}
else if(flag > 1)
{
printf("Case #%d: Bad magician!\n",z);
}
else
printf("Case #%d: Volunteer cheated!`\n",z);
z++;
}
return 0;
}
