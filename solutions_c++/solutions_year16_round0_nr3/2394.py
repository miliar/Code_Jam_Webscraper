#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<vector>
using namespace std;
typedef long long LL;
LL Convert(LL n, int base){
	LL m = 0, t = 1;
	for(; n; n >>= 1LL){
		m += (t * (n & 1LL));
		t *= (LL)base;
	}
	return m;
}
int T, N, J;
LL ans[11];
int main(){
	freopen("C_in.txt", "r", stdin);
	freopen("C_out.txt", "w", stdout);
	scanf("%d", &T);
	for(int C = 1; C<=T; ++C){
		scanf("%d%d", &N, &J);
		printf("Case #%d:\n", C);
		LL a = pow(2LL, (LL)(N-1)) + 1LL, b = pow(2LL, (LL)N);
		int cnt = 0;
		for(LL k = a; k<b; k+=2LL){
			int flag = 1;
			for(int base = 2; base<=10; ++base){
				ans[base] = 0LL;
				LL t = Convert(k, base);
				for(LL i = 2; i<=sqrt(t); i+=1LL)
					if(t % i == 0LL){
						ans[base] = i;
						break;
					}
				if(ans[base] == 0LL){
					flag = 0;
					break;
				}
			}
			if(flag){
				cnt++;
				int Bin[33];
				LL t = k;
				for(int i = N; i; i--){
					Bin[i] = t % 2;
					t >>= 1LL;
				}
				for(int i = 1; i<=N; ++i)
					printf("%d", Bin[i]);
				for(int i = 2; i<=10; ++i)
					printf(" %lld", ans[i]);
				printf("\n");
			}
			if(cnt>=J) break;
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
				
