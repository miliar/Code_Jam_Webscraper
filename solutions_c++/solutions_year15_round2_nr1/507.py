#include <cstdio>
#include <algorithm>

using namespace std;

long long reverse(long long a){
	long long ret = 0;
	while(a>0){
		ret*=10;
		ret+=a%10;
		a/=10;
	}
	return ret;
}

int digits(long long a){
	if(a == 0)return 1;
	int ret = 0;
	while(a>0){
		ret++;
		a/=10;
	}
	return ret;
}

long long goodtorev(long long a){
	int dg = digits(a);
	long long k = 1;
	for(int c = 0 ; c < dg/2; c++)
		k*=10;
	long long ret = a/k*k+1;
	// printf("%lld %lld\n",k,ret);
	return ret;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int cc = 1 ; cc <= T ; cc++){
		long long a;
		scanf(" %lld",&a);
		long long sol = 1;
		// printf("%lld\n",reverse(a));
		// printf("%d\n",digits(a));
		// goodtorev(a);
		while(a > 1){
			// printf("%lld,%lld\n",a,sol);
			long long b = goodtorev(a);
			if(b > a)sol++, a--;
			else if (b < a)sol += a-b, a = b;
			else if (a == reverse(a)) sol++, a--;
			else sol++, a = reverse(a);
		}
		printf("Case #%d: %lld\n",cc,sol);
	}
}