#include <bits/stdc++.h>
using namespace std;

#define MEM(arr,val)memset((arr),(val), sizeof (arr))
#define PI (acos(0)*2.0)
#define FASTER ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

ll gcd(ll a,ll b){return b == 0 ? a : gcd(b,a%b);}
ll lcm(ll a,ll b){return a*(b/gcd(a,b));}

/**
 * __builtin_popcount(int d) // count bits
 * __builtin_popcountll(long long d)
 * strtol(s, &end, base); // convert base number
 */
//----------------------------------------------------------------------//
#define MAXP 4000000
bitset<MAXP> isprime;
vi P;
void sieve(){
	isprime.set();
	isprime[1] = isprime[0] = 0;
	for (int i = 2; i*i < MAXP; ++i)
			if(isprime[i])
				for (int j = i*i; j < MAXP; j+=i)
					isprime[j] = 0;
	for (int i = 2; i < MAXP; ++i) {
		if(isprime[i])
			P.push_back(i);
	}
}

bool isPrime(ll n){

	if(n < MAXP)return isprime[n];

	for (int i = 0; i < P.size() && 1ll * P[i]* P[i] <= n; ++i) {
		if(n % P[i] == 0)return 0;
	}
	return 1;
}

int getDiv(ll n){

	if(n % 2 == 0)return 2;

	ll i = 3;
	while(i*i <= n){
		if(n % i == 0)return i;
		i++;
	}
//	printf("%lld: ", n);
//	for (int i = 0; i < P.size(); ++i) {
//		if(n % P[i] == 0)return P[i];
//	}
	return -1;
}

bool isjamcoin(string s){
//	printf("isjamcoin(%s)\n", s.c_str());
	for (int i = 2; i <= 10; ++i) {
		ll t = strtoll(s.c_str() , NULL, i);
//		printf("t = %lld (%d)\n", t, i);
		if(isPrime(t))return false;
	}
	return true;
}

void trivial(){

	int T;
	cin >> T;
	int Case = 1;
	while(T--){
		int J,N;
		cin >> N >> J;
		printf("Case #%d:\n", Case++);
//		printf("N = %d J = %d\n", N, J);

		int c = 0;

		for (int i = 0; i < (1ll << N) && c < J; ++i) {
			string coin;
			for (int j = 0; j < N; ++j)
				coin.push_back(((i&(1ll<<j)) != 0) + '0');

//			printf("debug: %s %d %d\n",coin.c_str(),i,c);

			if(coin.size() == N && coin[0] == '1' && coin[coin.size()-1] == '1' && isjamcoin(coin)){
				printf("%s", coin.c_str());
				for (int j = 2; j <= 10; ++j) {
					printf(" %d", getDiv( strtoll(coin.c_str(), NULL, j))  );
				}
				printf("\n");
				c++;
			}
		}



	}

}

int main(){
	FASTER;
	sieve();
	trivial();

	return 0;
}
