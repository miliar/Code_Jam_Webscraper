#include<iostream>
#include<stdio.h>
using namespace std;
int i,j,k,t,n,tt,i1,r,num;
int cal(int u)
{
    int s;
    s=2*u+1;
    return s; 
}
main()
{
      freopen("A-small-attempt0.in","r",stdin);
      freopen("A-small-attempt0.out","w",stdout);
      scanf("%d",&tt);
      for(i1=1;i1<=tt;i1++)
      {
                           k=0;j=0;num=0;
                           scanf("%d %d",&r,&t);
                           for(i=r;k==0;i=i+2)
                           {
                                              num++;
                                              j+=cal(i);
                                              if(j>t)k=1;
                           }
                           num--;
                           printf("Case #%d: %d\n",i1,num);
      }
      //system("pause");
}
