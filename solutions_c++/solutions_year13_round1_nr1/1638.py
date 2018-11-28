#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
int c,i,k,t,r,m;
scanf("%d",&m);
for(k=1;k<=m;k++)
{
  scanf("%d%d",&r,&t);
  c=0;
  while(1)
  {
    i=(2*r)+1;
    t-=i;
    if(t<0) break;
    c++;
    r+=2;
  }
  printf("Case #%d: %d\n",k,c);
}
return 0;
}
