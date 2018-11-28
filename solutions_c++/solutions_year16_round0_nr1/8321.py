#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(){
	int cases;
	scanf("%d", &cases);

	for(int e = 0; e<cases; e++){
		ll N;
		scanf("%lld", &N);

		if(!N){
			printf("Case #%d: INSOMNIA\n", e+1);
			continue;
		}

		vector<bool> taken(10, false);
		bool found = false;

		ll i = 1;
		while(!found){

			ll n = i * N;

			while(n){
				int dig = n % 10;
				taken[dig] = true;
				n/=10;
			}

			int cnt = 0;
			for(int i = 0; i<10; i++){
				if(taken[i]){
					cnt++;
				}
			}
			if(cnt == 10){
				found = true;
				printf("Case #%d: %lld\n", e+1, i*N);
				break;
			}

			i++;
		}


	}



	return 0;
}