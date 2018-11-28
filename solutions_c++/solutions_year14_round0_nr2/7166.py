/**********
rudra101 : The crownless again shall be the King !
**********/

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#define eps 1e-11
using namespace std;

int main()
{
freopen("B-large.in","r",stdin);
freopen("Out.txt","w",stdout);
  int t,i,j,n,k=1; 
  double Rate,val,c,f,x,Min; 
 scanf("%d",&t);
while(t--)
{
  scanf("%lf%lf%lf",&c,&f,&x);
 Min=x/2.0;
Rate=2;
val=c/2;
for(i=1;i<=1000000;i++)
{
Rate+=f;
val+=c/Rate;
Min=min(Min,val+(x-c)/Rate);
}
printf("Case #%d: %0.7lf\n",k++,Min);
}
 return 0;
}


