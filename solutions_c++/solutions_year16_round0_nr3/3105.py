#include<iostream>
#include<cmath>
#include<vector>

using namespace std;

typedef long long ll;

ll mul_mod (ll base, ll n, ll mod) {
	ll x = 0, y = base%mod;
	while (n>0) {
		if(n%2==1)	x = (x+y)%mod;
		y = (y*2)%mod;
		n /= 2;
	}
	return x%mod;
}

ll fast_modulo(int a,int b,long long c){
    long long x=1,y=a; // long long is taken to avoid overflow of intermediate results
    while(b > 0){
        if(b%2 == 1){
            x=mul_mod(x,y,c);
        }
        y = mul_mod(y,y,c); // squaring the base
        b /= 2;
    }
    return x%c;
}

int main()
{
	ios::sync_with_stdio(false);
	int t; cin >> t;
	cout << "Case #1: \n";
	int n, j; cin >> n >> j;
	string number(n,'0');
	number[0] = '1'; number[n-1] = '1';
	int count = 0;
	while (count!=j) {
		vector<int> active_bits;
		active_bits.push_back(0);
		for (int i = n-2; i > 0; i--) 
			if (number[i]=='1')
				active_bits.push_back(n-i-1);
		active_bits.push_back(n-1);
		bool is_legal = true;
		vector<ll> factors;
		for (int i = 2; i <= 10; i++) {
			ll check_till = pow(i,n/2);
			bool is_prime = true;
			for (ll k = 2; k*k <= check_till; k++) {
				ll rem = 0;
				for (int l = 0; l < active_bits.size(); l++)
					rem = (rem+fast_modulo(i,active_bits[l],k))%k;
				if (rem==0) {
					factors.push_back(k);
					is_prime = false;
					break;
				}
			}
			if (is_prime) {is_legal = false;break;}
		}
		if(is_legal) {
			cout << number << " ";
			for (int i = 0; i < factors.size(); i++)	cout << factors[i] << " ";
			cout << "\n";
			count++;
		}
		int p = n-2;
		while(p>=0 && number[p]=='1') {
			number[p]= '0';
			p--;
		}
		number[p] = '1';
	}
}
