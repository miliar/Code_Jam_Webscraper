// b@ver
#include<cstdio>
#include<iostream>
#include<algorithm>
#include <cmath>
#include <vector>
#include<cstring>
#include<cstdlib>
using namespace std;
int arr[4];
int main()
{
   int t,var;
   freopen("A-small-attempt1.in","r",stdin);
   scanf("%d",&t);
   var=t;
   while(t--)
   {
     // cout<<"t="<<t<<endl;
      int a1,a2,i,j,temp,flag=0,val,k;
      scanf("%d",&a1);
      for(i=0;i<4;i++)
      {
         for(j=0;j<4;j++)
         {
            scanf("%d",&temp);
            if(i==a1-1)
               arr[j]=temp;
         }
      }
      scanf("%d",&a2);
      for(i=0;i<4;i++)
      {
         for(j=0;j<4;j++)
         {
            scanf("%d",&temp);
            if(i==a2-1)
            {
               for(k=0;k<4;k++)
               {
                  if(temp==arr[k])
                  {
                     val=temp;
                     flag+=1;
                  }
               }
            }
         }
      }
      if(flag==0)
      {
         printf("Case #%d: Volunteer cheated!\n",var-t);
      }
      else if(flag==1)
      {
         printf("Case #%d: %d\n",(var-t),val);
      }
      else
      {
         printf("Case #%d: Bad magician!\n",var-t);
      }

   }
   return 0;
}
