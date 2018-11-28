#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
  int T;
  scanf("%d",&T);
  for(int C=1;C<=T;C++){
    long long x[37]={0};
    long long B;
    int N;
    scanf("%lld%d",&B,&N);
    for(int i=0;i<N;i++){
      scanf("%lld",x+i);
    }
    sort(x,x+37);
    double Max=0;
    for(int i=0;i<36;i++){
      long long K=0;
      for(int k=0;k<i;k++){
	K+=x[i]-x[k];
      }
      for(int k=i+1;k<37&&x[k]==x[i];k++){
	K++;
      }
      if(K>B){
	continue;
      }
      long long l=x[i],r=x[36];
      while(l+1<r){
	long long m=(l+r)/2,K=0;
	for(int k=0;k<=i;k++){
	  K+=m-x[k];
	}
	for(int k=i+1;k<37&&x[k]<m+1;k++){
	  K+=m+1-x[k];
	}
	if(K<=B){
	  l=m;
	}
	else{
	  r=m;
	}
      }
      long long P=0,Q=0;
      for(int k=0;k<=i;k++){
	P+=l-x[k];
	Q+=l-x[k];
      }
      for(int k=i+1;k<37&&x[k]<l+1;k++){
	Q+=l+1-x[k];
      }
      double E=(double)P*36./(i+1)-Q;
      if(E>Max){
	Max=E;
      }
    }
    printf("Case #%d: %.10lf\n",C,Max);
  }
  return 0;
}
