#include <cstdio>
#include <algorithm>

long long num[40];

long long calNeed(long long level, int en){

	long long ret = 0;
	for(int i = 0; i < en; i++){
		ret += level - num[i];
	}
	for(int i = en; i < 37; i++){
		if(level >= num[i]) ret += level + 1 - num[i];
	}
	return ret;

}

double test(int en, long long b){
	
	if(num[en-1] == num[36]) return 0;
	if(calNeed(num[en-1], en) > b) return 0;

	long long R = num[36] - 1;
	long long L = num[en-1];
	while(L != R){
		long long M = (L + R) / 2 + 1;
		if(calNeed(M, en) > b) R = M - 1;
		else L = M;
	}

	double ans = 0;
	for(int i = 0; i < en; i++) ans += 36 * (L - num[i]);
	//printf("en=%d, L=%lld, need=%lld, ans=%f\n" ,en ,L ,calNeed(L, en) ,ans / en - calNeed(L, en));
	return ans / en - calNeed(L, en);

}

int main(){

	int T;
	scanf("%d" ,&T);

	for(int t = 1; t <= T; t++){

		int n;
		long long b;
		scanf("%lld %d" ,&b ,&n);

		for(int i = n; i < 37; i++) num[i] = 0;
		for(int i = 0; i < n; i++) scanf("%lld" ,&num[i]);
		std::sort(num, num + 37);

		double ans = 0;
		for(int i = 1; i < 36; i++) ans = std::max(test(i, b), ans);
		printf("Case #%d: %.9f\n" ,t ,ans);

	}

}
