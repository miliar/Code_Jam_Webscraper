#include <iostream>
#include <set>
#include <bitset>
#include <vector>

using namespace std;

#define For(i, od, po) for(int (i) = (od); (i) < (po); (i)++)

typedef long long ll;

vector<ll> del(11);
ll n, j;

bool isOk(ll &x){
	bitset<32> b(x);
//	cout << "b = " << b << endl;
	bool ok = true;
	For(i, 2, 11){	
		ll cis = 0;
		ll agg = 1;
		
		// string to int
		for(ll k = 0; k <= n; k++){
			if(b[k]) cis += agg;
			agg *= i;
		}

//		cout << "cis = " << cis << " v " << i << " sustave" << endl;

		// is prime
		bool isPrime = true;
		for(ll k = 2L; k*k <= cis; k++){
			ll d = cis / k;

			/*if(k == 7){ cout << "d = " << d << "  k= " << k << "   * = "  
					<< k * d;
				cout << " je to ok? " << ( k * d == cis ? "ano" : "nie") <<endl;
				if(k * d == cis) cout << "ale ano 1\n";
			}*/
			if( k * d == cis){
		//		cout << "ale ano 2\n";
		//		cout << "cis = " << cis << "   d = " << d << "  k= " << k << "   * = "  << k * d;
				ok = false;
				del[i] = k;
				isPrime = false;
				break;
			}
		}	
//		if(isPrime) cout << " je prvocislo\n";
		if(isPrime) return false;
//		cout << " neni prvocislo " << cis << " " <<  b <<  "  delil som ho: " << del[i] << endl; 
	}
	return true;
}

void solve(int t){
	cout << "Case #1:\n";
	cin >> n >> j;
	n--;
	ll x = (1L << n) + 1;
	while(j && x < (1L << (n+1))){
		if(isOk(x)){
			j--;
	//		cout << "nasiel:   ";
			bitset<34> b(x);
			for(int i = n; i >= 0; i--) cout << b[i]; 
			For(i, 2, 11) cout << " " << del[i];
			cout << endl;
		}
		x += 2;
	}
	return;
}

int main(){
	int T;
	cin >> T;
	For(i, 0, T) solve(i+1);
	return 0;
}