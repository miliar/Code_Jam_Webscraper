#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdio>
#include <string>
#include <memory.h>
#include <algorithm>
using namespace std;
typedef pair<int,int> pii;
int t,tt,n,q,r,s,i,j,a[1000100];
long long p,cz,cur,res,sum;
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%I64d%d%d%d",&n,&p,&q,&r,&s);
    for (sum=i=0; i<n; i++) {
      a[i]=(i*p+q)%r+s;
      sum+=a[i];
    }
    for (res=cur=cz=i=j=0; i<n; i++) {
      cur+=a[i];
      while (j<i && max(cur-cz-a[j],cz+a[j])<max(cur-cz,cz)) cz+=a[j++];
      res=max(res,sum-max(sum-cur,max(cur-cz,cz)));
    }
    printf("Case #%d: %.10lf\n",t,(double)res/(double)sum);
  }
  return 0;
}
