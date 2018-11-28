#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main()
{
    int T, r, t, count, p;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
              scanf("%d%d",&r,&t);
              count=0;
              while(t>0)
              {
                        p=(r+1)*(r+1)-(r*r);
                        t=t-p;
                        if(t>=0)
                               count++;
                        r=r+2;
              }
              printf("Case #%d: %d\n",i,count);
    }
}
              
              
