#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int a[4][4];
int b[4][4];
int h1[16];
int h2[16];

int main()
{
    int t,ct;
    scanf("%d",&t);
    ct=1;
    while(t--)
    {
       int i,j,r1,r2;
       scanf("%d",&r1);

       for(i=0;i<4;i++)
       for(j=0;j<4;j++)
       scanf("%d",&a[i][j]);

       for(i=0;i<16;i++)
       h1[i]=h2[i]=0;

       scanf("%d",&r2);

       for(i=0;i<4;i++)
       for(j=0;j<4;j++)
       scanf("%d",&b[i][j]);

       int flag=0;
       int r=0;
       for(j=0;j<4;j++)
       {
           h1[a[r1-1][j]-1]=1;
           h2[b[r2-1][j]-1]=1;
       }


       for(i=0;i<16;i++)
       if(h1[i]==h2[i]&&h1[i]==1)
       {
           flag++;
           r=i+1;
       }

       if(flag==1)
       printf("Case #%d: %d\n",ct,r);
       else if(flag==0)
       printf("Case #%d: Volunteer cheated!\n",ct);
       else printf("Case #%d: Bad magician!\n",ct);
       ct++;
    }
    return 0;
}
