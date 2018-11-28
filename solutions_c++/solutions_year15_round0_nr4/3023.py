#include<iostream>
#include<stdio.h>
using namespace std;
int a[4][4]={
             {1,2,1,2},
             {2,2,2,2},
             {1,2,1,2},
             {2,2,2,2}};
int b[4][4]={
             {1,1,1,1},
             {1,1,2,1},
             {1,2,2,2},
             {1,1,2,1}};
int d[4][4]={
             {1,1,1,1},
             {1,1,1,1},
             {1,1,1,2},
             {1,1,2,2}};
int main()
{
    int t,x,r,c,k=1,ans;
    scanf("%d",&t);
    while(t--)
    {
       scanf("%d %d %d",&x,&r,&c);         
       if(x==1)
         ans=2;
       else 
       {
          if(x==2)
            ans=a[r-1][c-1];
          else if(x==3)
            ans=b[r-1][c-1];
          else
            ans=d[r-1][c-1];
       }
       if(ans==2)
          printf("Case #%d: GABRIEL\n",k);
       else
          printf("Case #%d: RICHARD\n",k);
       k++;
    }
 //  system("Pause");
   return 0;   
}
