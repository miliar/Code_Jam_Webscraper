#include<iostream>
#include<stdio.h>
using namespace std;

struct ps
{
   int fl;
   int n;
}pos[1<<5];



bool srt(ps a, ps b)
{
   if(a.fl<b.fl)
   {
      return 0;
   }
   else
   {
      if(a.fl==b.fl)
      {
         if(a.n<b.n)
         {
            return 0;
         }
         else
         {
            return 1;
         }
      }
      else
      {
         return 1;
      }
   }
}

int main ()
{
    
   freopen ("A-small-attempt0.in", "r", stdin);
   freopen ("A-small.out", "w", stdout);
   
   
   int t,k,i,r,a[1<<3][1<<3],n=4,j,p;
   cin>>t;
   for(k=1;k<=t;k++)
   {
      for(i=1;i<=16;i++)
      {
         pos[i].fl=0;
         pos[i].n=i;
      }
      
      scanf("%d",&r);
      for(i=1;i<=n;i++)
      {
         for(j=1;j<=n;j++)
         {
            scanf("%d",&a[i][j]);
         }
      }
      for(i=1;i<=n;i++)
      {
         pos[a[r][i]].fl++;
      }
      
      scanf("%d",&r);
      for(i=1;i<=n;i++)
      {
         for(j=1;j<=n;j++)
         {
            scanf("%d",&a[i][j]);
         }
      }
      
      for(i=1;i<=n;i++)
      {
         pos[a[r][i]].fl++;
      }
      
      sort(pos+1,pos+17,srt);
      
      /*for(i=1;i<=n;i++)
      {
         cout<<pos[i].fl<<" ";
         cout<<endl;
      }*/
      
      if(pos[1].fl==1)
      {
         printf("Case #");
         printf("%d",k);
         printf(": ");
         printf("Volunteer cheated!\n");
      }
      else
      {
         if(pos[2].fl==2)
         {
            printf("Case #");
            printf("%d",k);
            printf(": ");
            printf("Bad magician!\n");
         }
         else
         {
            printf("Case #");
            printf("%d",k);
            printf(": ");
            printf("%d\n",pos[1].n);
         }
      }
   }
   
   
   //system("pause");
   return 0;
}
