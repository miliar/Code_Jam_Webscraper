#include <iostream>
#include <memory.h>
#include <math.h>
using namespace std;

typedef long long ll;

int N, J;
bool base2[40];
ll fact[20];

void to2(int n){
	int lBase2 = 0;
	bool tmp[40];
	while(n > 0){
		tmp[lBase2 ++] = n % 2;
		n /= 2;
	}
	memset(base2, 0, sizeof(base2));
	for(int i = 0; i < lBase2; i ++)
		base2[i + N - lBase2 - 1] = tmp[lBase2 - 1 - i];
	base2[0] = base2[N - 1] = 1;
}

bool checkPrime(ll r, int k){
	if(r == 2)
		return true;
	for(ll i = sqrt(r); i >= 2; i --)
		if(r % i == 0){
			fact[k] = i;
			return false;
		}
	return true;
}

ll interpretTo(ll k){
	ll ret = 0;
	for(int i = 0; i < N; i ++){
		ret = ret * k + base2[i];
	}
	return ret;
}

int main(){
	int t;
	cin >> t;
	for(int i = 1; i <= t; i ++){
		cout << "Case #" << i << ":\n";
		cin >> N >> J;
		for(int j = 0; j <= (1 << (N - 2)) - 1 && J > 0; j ++){
			to2(j);
			int k;
			for(k = 2; k <= 10; k ++){
				ll r = interpretTo(k);
				if(checkPrime(r, k))
					break;
			}
			if(k <= 10)
				continue;
			for(int k = 0; k < N; k ++)
				cout << base2[k];
			cout << " ";
			for(int k = 2; k <= 10; k ++)
				cout << fact[k] << " ";
			cout << endl;
			J --;
		}
	}

	return 0;
}

