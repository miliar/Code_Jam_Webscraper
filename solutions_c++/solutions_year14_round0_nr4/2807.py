#include <cstdio>
#include <algorithm>
using namespace std;

long n;
long cari(double x[], double y[]){
	long res=0;
	bool bol[1005]={};
	for(long i=0; i<n; i++){
		long p=-1,b=-1;
		for(long j=0; j<n; j++){
			if((y[j]<y[b] || b==-1) && !bol[j]) b=j;
			if(((y[j]>x[i] && p==-1) || (y[p]>y[j]>x[i])) && !bol[j]) p=j;
		}
		if(p==-1){
			bol[b] = 1;
			res++;
		} else bol[p] = 1;
	}
	return res;
}

int main(){
	long t;
	scanf("%ld",&t);
	for(long g=1; g<=t; g++){
		double x[1005],y[1005],z[1005];
		scanf("%ld",&n);
		for(long i=0; i<n; i++)
			scanf("%lf",&x[i]);
		for(long i=0; i<n; i++)
			scanf("%lf",&y[i]);
		sort(x,x+n); sort(y,y+n);
		printf("Case #%ld: %ld %ld\n",g,n-cari(y,x),cari(x,y));
	}
	return 0;
}