#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>

#define io_r freopen("input.txt","r",stdin);
#define io_w freopen("output.txt","w",stdout);
#define io_file io_r; io_w;

#define PB push_back
#define MP make_pair
#define ll long long

#define rep(i,n) for (int i = 0; i<n; ++i)
#define clr(x, y) memset(x, y, sizeof x)
#define all(x) (x).begin(), (x).end()

#define MAX 10000010
#define MOD 1000000007

using namespace std;

vector <ll> primes;
bool *isprime = new bool[MAX+10];

void sieve (){
	unsigned ll i, j;

	for (i = 0; i<=MAX; i++) isprime[i] = true;

	isprime[0] = isprime[1] = false;

	primes.PB (2);
	for (i = 4; i<=MAX; i += 2) isprime[i] = false;

	for (i = 3; i<=MAX; i += 2){
		if (isprime[i]){
			primes.PB (i);
			for (j = i*i; j<MAX; j += i)
				isprime[j] = false;
		}
	}

}

ll convert(int bin, int base, int sz){
	ll b = 1;
	ll ans = 0;
	
	rep(i, sz){
		ans += ((1<<i)&bin ? 1 : 0)*b;
		b = (ll) b * base;
	}
	
	return ans;
}

#define f(i,a,b) for (int i = a; i<b; i++)
ll divisors (ll n){

	ll sq_div = (ll) sqrt (n) + 1;
	
	f (i, 2, sq_div) if (n%i == 0){
		return i;
	}
	
	return -1;
}

bool checkIsPrime (ll n){
	ll aux = n;
	int i = 0;
	
	int count = 0;
	
	while (i < primes.size() && primes[i]*primes[i] <= n){
		if (aux%primes[i] == 0){
			while (aux%primes[i] == 0) {
				aux /= primes[i];
				count++;
			}
			
			if(count > 1) return false;
		}
		
		i++;
	}
	
	if (aux > 1) count++;
	
	return count > 1 ? false : true;
}

bool valid(int n, int sz){
	for(int i = 2; i<=10; i++){
		ll x = convert(n, i, sz);
		if(checkIsPrime(x)) return false;
	}
	return true;
}

int main (){
	sieve();
	
	int n = 16;
	int J = 50;
	
	puts("Case #1:");
	for(int i = 0; i<(1<<(n+1)) && J > 0; i++){
		if((1<<0)&i && (1<<(n-1))&i && valid(i, n)){
			printf("%lld", convert(i, 10, n));
			for(int j = 2;  j<=10; j++){
				ll x = convert(i, j, n);
				ll y = divisors(x);
				printf(" %lld", y);
			}
			puts("");
			J--;
		}
	}
	
	
	return 0;
}
