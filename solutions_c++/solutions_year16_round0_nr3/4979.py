#include <bits/stdc++.h>

using namespace std;

#define ll				long long int
#define vi				vector<int>
#define vl				vector<ll>
#define pii				pair<int,int>
#define pil				pair<int, ll>
#define pll				pair<ll, ll>
#define pli				pair<ll, int>
#define pb				push_back
#define mp				make_pair
#define MOD				1000000007
#define F				first
#define S				second


int check(ll var, ll pos){

	if(((var) & (1<<(pos))))
		return 1;
	else
		return 0;
	

}

int is_prime(ll num){

	return 1;
}

ll pow_mod(ll a, ll b) {
	ll res = 1;
	while(b) {
		if(b & 1)
			res = (res * a);
		a = (a * a);
		b >>= 1;
	}
	return res;
}

int main(){

	ll t = 1;
	scanf("%lld", &t);

	ll n = 16,J = 50;
	scanf("%lld %lld", &n, &J);

	ll lim = 1 << 16;

	vector < pair < ll, vector < ll > > > ans;

	for(ll i = 1;i < lim;i++){

		if(check(i, 0) && check(i,15)){

			vector < ll > proof;
			ll res, p_flag = 1;

			for(ll base = 2; base <= 10;base++){

				ll num = 0;
				ll val = 1;

				for(ll j = 0;j<16;j++){
					num += check(i,j)*val;
					val *= base;
				}

				int flag = 1;

				for(int k=2;k < (int)sqrt(num) + 1;k++){
					if(num%k==0){
						flag = 0;
						proof.pb(k);
						break;
					}
				}

				if(flag == 0){
					if(base == 10)
						res = num; 
				}
				else{
					p_flag = 0;
					break;
				}

			}

			if(p_flag && proof.size() == 9)
				ans.pb(mp(res, proof));
		}

		if(ans.size() == 50)
			break;

	}

	printf("Case #1:\n");
	assert(ans.size() == 50);

	for(int i = 0;i<50;i++){
		printf("%lld ", ans[i].F);
		for(int j=0;j<9;j++)
			printf("%lld ", ans[i].S[j]);
		printf("\n");
	}


	return 0;
}
