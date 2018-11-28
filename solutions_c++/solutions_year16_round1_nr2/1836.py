#include <bits/stdc++.h>
#define pb push_back
#define popb pop_back
#define mkp make_pair
#define par pair<ll, ll>
#define N 200010

typedef long long ll;

using namespace std;

ll ocorrencia[N];

int main(){

	ll n, m, i, k, j, x;

	scanf("%lld\n", &n);

	for(k = 1; k <= n; k++){
		scanf("%lld", &m);
		for(i = 0; i < N; i++){
			ocorrencia[i] = 0;
		}

		for(i = 0; i < 2*m-1; i++){
			for(j = 0; j < m; j++){
				scanf("%lld", &x);
				ocorrencia[x]++;
			}
		}

		printf("Case #%lld:", k);
		for(i = 0; i < N; i++){
			if(ocorrencia[i] % 2 != 0)
				printf(" %lld", i);
		}

		printf("\n");
	}
	return 0;
}
