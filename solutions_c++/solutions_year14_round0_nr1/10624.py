#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
int ar[4][4],t,n1,n2,j,k,index,temp1[4],p=1;
scanf("%d",&t);
while(p<=t)
{
index=0;
scanf("%d",&n1);
for(j=0;j<4;j++)
{
for(k=0;k<4;k++)
{
scanf("%d",&ar[j][k]);
}
}
temp1[0]=ar[n1-1][0];temp1[1]=ar[n1-1][1];temp1[2]=ar[n1-1][2];temp1[3]=ar[n1-1][3];
scanf("%d",&n2);
for(j=0;j<4;j++)
{
for(k=0;k<4;k++)
{
scanf("%d",&ar[j][k]);
}
}

for(j=0;j<4;j++)
{
for(k=0;k<4;k++)
{
if(temp1[j]==ar[n2-1][k])
{index++;n1=temp1[j];}
}
}

if(index==1)
printf("Case #%d: %d\n",p,n1);

else if(index>1)
printf("Case #%d: Bad magician!\n",p);

else if(index==0)
printf("Case #%d: Volunteer cheated!\n",p);

p++;
}
return 0;
}
