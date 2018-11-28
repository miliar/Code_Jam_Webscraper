#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#define ll long long
using namespace std;

ll convert(ll input, int base)
{
	ll sum = 0, temp = 1;
	while(input > 0) {
		if(input & 1) sum += temp;
		input >>= 1;
		temp *= (ll)base;
	}
	return sum;
}

ll get_divisor(ll input)
{
	ll u_bound = (ll)sqrt(input);
	for(ll i = 2; i <= u_bound; i++) {
		if(input % i == 0) return i;
	}
	return -1;
}

class PrimalityTest
{
private:
	ll mulmod(ll a, ll b, ll mod){
    	ll x = 0,y = a % mod;
    	while (b > 0){
        	if (b % 2 == 1) x = (x + y) % mod;
        	y = (y * 2) % mod;
        	b /= 2;
        }
        return x % mod;
    }

	ll modulo(ll base, ll exponent, ll mod){
    	ll x = 1;
    	ll y = base;
    	while (exponent > 0){
        	if (exponent % 2 == 1) x = mulmod(x, y, mod);
        	y = mulmod(y, y, mod);
        	exponent = exponent / 2;
    	}
    	return x % mod;
    }

public:
	bool Miller(ll p, int iteration){
		if (p < 2) return false;
    	if (p != 2 && p % 2==0) return false;
    	ll s = p - 1;
    	while (s % 2 == 0) s /= 2;
    	for (int i = 0; i < iteration; i++){
        	ll a = rand() % (p - 1) + 1, temp = s;
        	ll mod = modulo(a, temp, p);
        	while (temp != p - 1 && mod != 1 && mod != p - 1){
            	mod = mulmod(mod, mod, p);
            	temp *= 2;
        	}
        	if (mod != p - 1 && temp % 2 == 0) return false;
    	}
    	return true;
    }
};

void print_bin(int n)
{
    int l = sizeof(n)*8;
    int i;
    if(i == 0)
    {
         printf("0");
         return;
     }
    for(i = l-1; i >= 0; i --)
    {
        if(n&(1<<i)) break;
    }

    for(;i>=0; i --)
        printf("%d", (n&(1<<i)) != 0);
}

int main()
{
	int casenum, N, J;

	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cin >> casenum;
	for(int i = 1; i <= casenum; i++) {
		printf("Case #%d:\n", i);
		cin >> N >> J;
		PrimalityTest pt = PrimalityTest();
		ll u_bound = (ll)pow(2, N);
		ll lower_bound = (ll)pow(2, N - 1) + 1;
		int cnt = 0;
		for(ll j = lower_bound; j < u_bound; j += 2) {
			bool flag = false;
			for(int k = 2; k <= 10; k++) {
				ll number = convert(j, k);
				if(pt.Miller(number, 5)) {flag = true; break;}
			}
			if(!flag) {
				print_bin((int)j);
				for(int k = 2; k <= 10; k++) printf(" %lld", get_divisor(convert(j, k)));
				cout << endl;
				cnt++;
				if(cnt == J) break;
			}
		}
	}

	return 0;
}

