#include<stdio.h>
#include<iostream>
using namespace std;
main()
{
  //1 , 4, 9, 121 (11), 484 (22), 10201 (101), 12321 (111)  
  int t,a,b,x=0;
  scanf("%d",&t);
  while(t--)
  {
    scanf("%d%d",&a,&b);
    int count=0;
    if(1>=a && 1<=b)
      count++;
    if(4>=a && 4<=b)
      count++;
    if(9>=a && 9<=b)
      count++;
    if(121>=a && 121<=b)
      count++;
    if(484>=a && 484<=b)
      count++;
    
    printf("Case #%d: %d\n",++x,count);
  }
  return 0;
}