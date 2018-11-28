#include <cstdio>

int main(){
	long n;
	scanf("%ld",&n);
	for(long g=1; g<=n; g++){
		long a,b,k,res=0;
		scanf("%ld %ld %ld",&a,&b,&k);
		for(long i=0; i<a; i++)
			for(long j=0; j<b; j++)
				if((i&j)<k) res++;
		printf("Case #%ld: %ld\n",g,res);
	}
	return 0;
}