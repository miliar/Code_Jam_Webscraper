#include<cstdio>
#include<algorithm>
using namespace std;

double N[1400];
double K[1503];

int dw(int n){
	int m=0,ma=n-1,w=0;
	for(int i=0;i<n;i++){
		if(N[i]<K[m])ma--;
		else {
			w++;
			m++;
		}
	}
	return w;
}

int war(int n){
	int m=0,w=0;
	for(int i=0;i<n;i++){
		while(K[m]<N[i] && m<n)m++;
		if(m==n)return n-i;
		m++;
	}
}

void f(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)scanf("%lf",&N[i]);
	for(int i=0;i<n;i++)scanf("%lf",&K[i]);
	sort(N,N+n);
	sort(K,K+n);
//	for(int i=0;i<n;i++)printf("%lg ",N[i]);
//	printf("\n");
//	for(int i=0;i<n;i++)printf("%lg ",K[i]);
//	printf("\n");
//	printf("%d\n",war(n));
	printf("%d %d\n",dw(n),war(n));
}

int main(){
	int a;
	scanf("%d",&a);
	for(int i=1;i<=a;i++){
		printf("Case #%d: ",i);
		f();
	}
}
