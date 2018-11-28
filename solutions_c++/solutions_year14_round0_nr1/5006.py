#include<bits/stdc++.h>
#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
 // freopen("in", "r", stdin);
  //freopen("out", "w", stdout);

int t,p=0;
scanf("%d",&t);
while(t--)
{
p++;
 int row1,row2,mat1[10][10],mat2[10][10],i,j,c=0,save=-1,r1[10],r2[10];
scanf("%d",&row1);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
scanf("%d",&mat1[i][j]);

scanf("%d",&row2);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
scanf("%d",&mat2[i][j]);

for(j=0;j<4;j++)
r1[j]=mat1[row1-1][j];



for(j=0;j<4;j++)
r2[j]=mat2[row2-1][j];



for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(r1[i]==r2[j])
{
c++;
if(c==1)
save=r1[i];
}
}
}


if(c==1)
printf("Case #%d: %d\n",p,save);
else if(c==0)
printf("Case #%d: Volunteer cheated!\n",p);

else
printf("Case #%d: Bad magician!\n",p);
}

return 0;

  }
