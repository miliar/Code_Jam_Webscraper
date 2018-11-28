#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define p(x) cerr<<#x<<":"<<x<<"\n"
int cs,c,i,j,x,s,n;
int A[10001];
int main()
{
  scanf("%d",&cs);
  for(c=1;c<=cs;c++)
  {
    scanf("%d%d",&n,&x);
    for(i=0;i<n;i++)
      scanf("%d",&A[i]);
    sort(A,A+n);
    for(i=n-1,s=0,j=0;i>=j;s++)
    {
      if(A[i]+A[j]<=x)
       j++;
      i--;
    }
    printf("Case #%d: %d\n",c,s);
  }
	return 0;
}
