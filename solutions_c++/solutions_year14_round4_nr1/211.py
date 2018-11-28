#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <ctime>
#include <set>
#include <bitset>
#include <map>
#include <utility>
#include <iterator>
using namespace std;
int i,j,w,n;
int sum;
int a[300001];
int cmp(const void*v1,const void*v2)
{
    int t1=*(int*)v1,t2=*(int*)v2;
    return t2-t1;
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
   	 scanf("%d",&n);
   	 scanf("%d",&w);
   	 for (i=0;i<n;i++)scanf("%d",&a[i]);
   	 qsort(a,n,sizeof(int),cmp);
   	 i=0;j=n-1;
   	 sum=0;
  	  while (i<j)
  	  {
 	       if (a[i]+a[j]<=w)j--;
 	       i++;
 	       sum++;
    	}
    	if (i==j)sum++;
    	printf("Case #%d: %d\n",t,sum);
	}
    return 0;
}
