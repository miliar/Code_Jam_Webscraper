#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    int n;
    scanf("%d",&n);
    double a[1000],b[1000];
    for(int i=0;i<n;i++){
      scanf("%lf",a+i);
    }
    for(int j=0;j<n;j++){
      scanf("%lf",b+j);
    }
    sort(a,a+n);
    sort(b,b+n);
    int K=0;
    for(;K<n;K++){
      int x=0;
      for(;x<n-K;x++){
	if(a[K+x]<b[x]){
	  break;
	}
      }
      if(x==n-K){
	break;
      }
    }
    int k=0,l=0;
    for(;l<n;){
      if(b[l]<a[k]){
	l++;
      }
      else{
	k++;
	l++;
      }
    }
    printf("Case #%d: %d %d\n",t,n-K,n-k);
  }
  return 0;
}
