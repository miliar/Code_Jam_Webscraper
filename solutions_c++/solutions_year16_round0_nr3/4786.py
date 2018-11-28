#include <bits/stdc++.h>
using namespace std;

//Sieve of Eratosthenes - Geração de Numeros Primos
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;

ll sieve_size;
bitset<100000010> bs; //10^8 should be enought
vi primes; //compact list of primes in form of vector<int>

//create list of primes in [0..upperbound]
void sieve(ll upperbound) {
	
	sieve_size = upperbound + 1; //add 1 to include upperbound
	bs.set();
	bs[0] = bs[1] = 0; //obs: especific problems can consider "1" as a prime
	
	for (ll i = 2; i <= sieve_size; i++) {
		if (bs[i]) {
			// cross out multiples of i starting from i * i !
			for (ll j = i * i; j <= sieve_size; j += i) { bs[j] = 0; }
			primes.push_back(i);
		}
	}
}

//note: only work for N <= ( last prime in vi "primes" )^2
bool isPrime(ll N) {
	
	if (N <= sieve_size) { return bs[N]; }
	
	for (int i = 0; i < primes.size(); i++) {
		if (N % primes[i] == 0) { return false; }
	}
	
	return true;
}

//Fatoração em Primos - Rodar o Crivo de Eratostenes antes
ll primeFactors(ll N) {
	
	ll PF_idx = 0, PF = primes[PF_idx];
	ll Ni = N;
	ll resul = 0;
	bool bk = false;
	
	while (N != 1 && (PF * PF <= N)) {
		while (N%PF == 0) {
			N /= PF;
			if (PF != Ni) {
				resul = PF;
				bk = true;
				break;
			}
		}
		if (bk) { break; }
		PF = primes[++PF_idx];
	}
	
	if (N != Ni) { resul = N; }
	
	return resul;
}

int main() {
	
	sieve(100000000LL);
	double reg[12][20];
	
	for (int b = 2; b <= 10; b++) {
		for (int e = 0; e <= 18; e++) {
			reg[b][e] = -1;
		}
	}
	
	int T, N, J;
	scanf("%d", &T);
	 
	for (int i = 1; i <= T; i++) {
		scanf("%d %d", &N, &J);
		printf("Case #%d:\n", i);
		
		int mask = 1 << (N-1);
		int limit = (1 << N) - 1;
		int masks = 0;
		
		//mascaras
		for (mask; mask <= limit; mask++) {
			bool valid = true;
			string list = "";
			
			//bases
			for (int b = 2; b <= 10; b++) {
				double num = 0;
				
				//varrendo mascara de bits
				for (int j = 0; j < N; j++) {
					if ( mask & (1<<j) ) {
						if (reg[b][j] == -1) {
							reg[b][j] = pow(b,j);
						}
						num += reg[b][j];
					} else {
						if (j == 0) {
							valid = false;
							break;
						}
					}
				}
				
				if (!valid) { break; }
				
				if (isPrime(num)) {
					valid = false;
					break;
				} else {
					stringstream ss;
					string str = "";
					ss << primeFactors(num);
					ss >> str;
					list += (" " + str);
				}
			}
			
			if (valid) {
				string maskstr = bitset<16>(mask).to_string();
				maskstr = maskstr.substr(16-N, N);
				printf("%s%s\n", maskstr.c_str(), list.c_str());
				masks++;
				if (masks == J) { break; }
			}
		}
	}
	
	return 0;
}