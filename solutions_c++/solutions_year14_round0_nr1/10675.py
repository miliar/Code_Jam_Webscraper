#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
   int a[4][4],b[4][4],t,T,p1,p2,temp[4],temp1[4],c;
   scanf("%d",&T);
   for(int t=1;t<=T;t++)
   {
       int count=0;
       scanf("%d",&p1);
       for(int i=0;i<4;i++)
       {
           for(int j=0;j<4;j++)
           scanf("%d",&a[i][j]);
       }
       scanf("%d",&p2);
       for(int i=0;i<4;i++)
       {
           for(int j=0;j<4;j++)
           scanf("%d",&b[i][j]);
       }
       
       //printf("%d\t%d\n",p1,p2);
       for(int j=0;j<4;j++)
       {
          temp[j]=a[p1-1][j];
         // cout<<temp[j]<<"\n";
       }
       
       for(int j=0;j<4;j++)
       {
            temp1[j]=b[p2-1][j];
           // cout<<temp1[j]<<"\n";
       }
       for(int i=0;i<4;i++)
       {
           for(int j=0;j<4;j++)
       {
           if(temp[i]==temp1[j])
           {
             c=temp[i];
             count++;
            }
       }
            
       }
       
            if(count==1)
            printf("Case #%d: %d\n",t,c);
            else if(count>1)
            printf("Case #%d: Bad magician!\n",t);
            else if(count==0)
            printf("Case #%d: Volunteer cheated!\n",t);
       
       
   }
}
