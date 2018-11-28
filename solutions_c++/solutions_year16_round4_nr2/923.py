#include<bits/stdc++.h>
using namespace std;
double p[10000];
int v[1000];
int main(){
  int test;
  scanf("%d",&test);
  for(int t=1;t<=test;t++){
    int n,k;
    double maxi=0;
    scanf("%d%d",&n,&k);
    for(int i=1;i<=n;i++) scanf("%lf", &p[i]);
    for(int opt=0;opt<(1<<n);opt++){
      if(__builtin_popcount(opt)!=k) continue;
      int r=opt, ind=0;
      for(int j=1;j<=n and r;j++){
	if(r%2) v[ind++]=j;
	r/=2;
      }
      double sum=0;
      for(int ver=0;ver<(1<<k);ver++){
	if(__builtin_popcount(ver)!=k/2) continue;
	r=ver;
	int ile=0;
	double p1=1,p2=1;
	for(int j=0;j<k;j++){
	  if(r%2) {
	    p1*=p[v[j]];
	  }
	  else{
	    p2*=(1-p[v[j]]);
	  }
	  r/=2;
	}
	sum+=p1*p2;
      }
      maxi=max(maxi, sum);
    }
    printf("Case #%d: %.7lf\n", t, maxi);
  }
}