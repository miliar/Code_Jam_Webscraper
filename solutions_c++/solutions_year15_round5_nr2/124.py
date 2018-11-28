#include<stdio.h>
#include<algorithm>
using namespace std;
long long n, K, w[1010], L[1010];
int main(){
	long long TC, TT, i, b, e, x, s;
	long long SS, Sum;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%lld", &TC);
	for (TT = 1; TT <= TC; TT++){
		printf("Case #%lld: ", TT);
		scanf("%lld%lld", &n, &K);
		for (i = 1; i <= n - K + 1; i++){
			scanf("%lld", &w[i]);
		}
		SS = w[1];
		for (i = 1; i <= K; i++){
			b = 0, e = 0, s = 0;
			x = i;
			while (x + K <= n){
				s += w[x + 1] - w[x];
				if (b > s)b = s;
				if (e < s)e = s;
				x += K;
			}
			L[i] = e - b;
			SS += b;
		}
		if (SS < 0)SS += (-SS) / K*K + K;
		SS %= K;
		sort(L + 1, L + K + 1);
		Sum = 0;
		for (i = 1; i <= K; i++){
			Sum += L[K] - L[i];
			if (Sum >= SS)break;
		}
		if (i == K + 1){
			printf("%lld\n", L[K] + 1);
		}
		else printf("%lld\n", L[K]);
	}
}