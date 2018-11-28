#include <bits/stdc++.h>

using namespace std;

int main(){
	long long t, x, cont = 0;

	scanf("%lld", &t);

	while(t--){
		cont++;	
		vector<long long> vet;
		long long n;

		scanf("%lld", &n);

		while(n--){
			scanf("%lld", &x);
			vet.push_back(x);
		}

		long long l = 0;
		long long ma = 0;

		for(long long i = 0; i < vet.size() - 1; i++){
			long long a = vet[i] - vet[i + 1];

			if(a > 0){
				l += a;
				ma = max(ma, a);
			}
		}

		long long r = 0;
		
		for(long long i = 0; i < vet.size() - 1; i++){
			r += min(ma, vet[i]);
		}

		printf("Case #%lld: %lld %lld\n", cont, l, r);
	}

	return 0;
}
