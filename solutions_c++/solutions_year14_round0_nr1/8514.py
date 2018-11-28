#include<iostream>
//#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#define mod 1000000007
#include <vector>

using namespace std;

int main()
{
	freopen("D:/in.txt","r",stdin);
   freopen("D:/out.txt","w",stdout);
   int t,i,j,n,a,b,m;
	int c[4][4],d[4][4];

	scanf("%d",&t);
    for(int tc=1;tc<=t;++tc)
    {
       scanf("%d",&a);

		 for(i=0;i<4;++i)
         for(j=0;j<4;++j)
           scanf("%d",&c[i][j]);


       scanf("%d",&b);

		 for(i=0;i<4;++i)
         for(j=0;j<4;++j)
           scanf("%d",&d[i][j]);

       n=0;
       for(i=0;i<4;++i)
       {
          for(j=0;j<4;++j)
          {
             if(c[a-1][i]==d[b-1][j])
             {
                ++n;
                m=c[a-1][i];
                break;
             }
          }
       }

       if(n==0)
         printf("Case #%d: Volunteer cheated!\n",tc);
       else if(n==1)
         printf("Case #%d: %d\n",tc,m);
       else
         printf("Case #%d: Bad magician!\n",tc);

    }

	return 0;

}
