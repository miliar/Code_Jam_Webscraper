#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
int t,x,y,i,a[4][4],b[4][4],c,j,w[4],z[4],r,q;
freopen("A-small-attempt0.in.txt", "r", stdin);
freopen("output.txt", "w", stdout);
scanf("%d",&t);
for(q=1;q<=t;q++)
{    c=0;
     scanf("%d",&x);
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
for(i=0;i<4;i++)
{
    w[i]=a[x-1][i];
}
    scanf("%d",&y);
     for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            scanf("%d",&b[i][j]);
        }
    }
  for(i=0;i<4;i++)
{
    z[i]=b[y-1][i];
}
  for(i=0;i<4;i++)
  {
    for(j=0;j<4;j++)
    {
        if(z[i]==w[j])
        {c++;
        r=z[i];
        break;
        }
    }
  }
  if(c==1)
        printf("Case #%d: %d\n",q,r);
        else if(c==0)
        printf("Case #%d: Volunteer cheated!\n",q);
        else
        printf("Case #%d: Bad magician!\n",q);

}
return 0;
}

