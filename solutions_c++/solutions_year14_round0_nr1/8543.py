#include <stdio.h>

int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);    
    
int t,i,b,c[4][4],d[4][4],j,k,m;
scanf("%d",&t);

for(i=0;i<t;i++)
{

if(i!=0)
printf("\n");

scanf("%d",&b);

for(j=0;j<4;j++)
{
for(k=0;k<4;k++)
{
scanf("%d",&c[j][k]);
}
}

scanf("%d",&m);

for(j=0;j<4;j++)
{
for(k=0;k<4;k++)
{
scanf("%d",&d[j][k]);
}
}

int count=0,ans;

for(j=0;j<4;j++)
{
for(k=0;k<4;k++)
{

if(c[b-1][j]==d[m-1][k])
{
count=count+1;
ans=c[b-1][j];
}

}
}




if(count==0)
printf("Case #%d: Volunteer cheated!",i+1);

else if(count==1)
printf("Case #%d: %d",i+1,ans);

else
printf("Case #%d: Bad magician!",i+1);

}


return 0;
}
