#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cerr<<#x<<":"<<x<<"\n"
int cs,c,i,j,r,x,s;
int C[17];
int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    memset(C,0,sizeof C);
    scanf("%d",&r);
    for(i=1;i<=4;i++)
      for(j=1;j<=4;j++)
      {
        scanf("%d",&x);
        if(i==r)
          C[x]++;
      }
    scanf("%d",&r);
    for(i=1;i<=4;i++)
      for(j=1;j<=4;j++)
      {
        scanf("%d",&x);
        if(i==r)
          C[x]++;
      }
    for(s=0,i=1;i<=16;i++)
      if(C[i]==2)
      {
        s++;
        j=i;
      }
    printf("Case #%d: ",c);
    if(s==0)
      printf("Volunteer cheated!\n");
    else if(s==1)
      printf("%d\n",j);
    else
      printf("Bad magician!\n");
  }
	return 0;
}
