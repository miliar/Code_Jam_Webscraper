#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
int t,grid1[4][4],grid[4][4],k,l,m,n;
scanf("%d",&t);
int r=1;
while(r<=t)
{l=0;k=0;
scanf("%d",&m);
for(int i=1;i<=4;i++)
{for(int j=1;j<=4;j++)
scanf("%d",&grid1[i][j]);
}
scanf("%d",&n);
for(int i=1;i<=4;i++)
{for(int j=1;j<=4;j++)
scanf("%d",&grid[i][j]);
}
for(int i=1;i<=4;i++)
{for(int j=1;j<=4;j++)
{if(grid1[m][i]==grid[n][j])
{l=grid1[m][i];
k++;
}
}
}

if(k==0)
printf("Case #%d: Volunteer cheated!\n",r);
if(k==1)
printf("Case #%d: %d\n",r,l);
if(k>1)
printf("Case #%d: Bad magician!\n",r);
r++;
}
return 0;
}
