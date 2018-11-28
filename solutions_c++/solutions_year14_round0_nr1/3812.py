#include<bits/stdc++.h>
int main() {
int t,increment=0;
scanf("%d",&t);
while(t--)
{
increment++;
int rr,rx,aa[10][10],bb[10][10],i,j,c=0,ans=-1,r1[10],r2[10];
scanf("%d",&rr);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
scanf("%d",&aa[i][j]);
scanf("%d",&rx);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
scanf("%d",&bb[i][j]);
for(j=0;j<4;j++)
r1[j]=aa[rr-1][j];
for(j=0;j<4;j++)
r2[j]=bb[rx-1][j];
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(r1[i]==r2[j])
{
c++;
if(c==1)
ans=r1[i];
}
}
}
if(c==1)
printf("Case #%d: %d\n",increment,ans);
else if(c==0)
printf("Case #%d: Volunteer cheated!\n",increment);
else
printf("Case #%d: Bad magician!\n",increment);
}
return 0;
}
