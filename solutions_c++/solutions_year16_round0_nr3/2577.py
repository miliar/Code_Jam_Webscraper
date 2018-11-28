#include <bits/stdc++.h>

using namespace std;

#define INP "inp.txt"
#define OUT "out2.txt"
#define MAXN 16
#define MAXJ 50
#define MAXSIEVE 100000000ll
#define ll long long
#define ROOT 10

int T, N, J, b[MAXN];
ll root[ROOT + 1][MAXN], ss;
bitset<100000100> bs;
std::vector<int> primes;

ll convertBase(int b[], int base) {
	ll res = 0ll;
	for(int i = 0, j = MAXN - 1; i < MAXN; i++, j--) {
		res += b[i] * root[base][j];
	}
	return res;
}

void sieve(ll upperbound) {
	ss = upperbound + 1; 
	bs.reset(); bs.flip();
	bs.set(0, false); bs.set(1, false); 
	for (ll i = 2; i <= ss; i++) if (bs.test((size_t)i)) {
		for (ll j = i * i; j <= ss; j += i) bs.set((size_t)j, false);
		primes.push_back((int)i);
	}
}

bool isPrime(ll N) {	
	if (N < ss) return bs.test(N);
	int s = primes.size();
	for (int i = 0; i < primes.size() - 1; i++) if (N % primes[i] == 0) return false;
	return true; 
}

void nextBitSet() {
	int start = MAXN - 2;
	while(b[start]) {
		b[start--] = 0;
	}
	b[start] = 1;
}

int findFirstPrimeFactor(ll N) {
	for(int i = 0; i < primes.size(); i++) {
		if(N % primes[i] == 0) return primes[i];
	}
}

void preCal() {
	cout << "Case #1:" << endl;
    //set up sieve
    sieve(MAXSIEVE);

	//set up root array
	for(int i = 2; i <= ROOT; i++) {
		root[i][0] = 1ll;
		for(int j = 1; j < MAXN; j++) {
			root[i][j] = root[i][j - 1] * i;
		}
	}

	int cnt = 0;
	b[0] = b[MAXN - 1] = 1;

	while(true) {
		int ok = 1;
		for(int i = 2; i <= ROOT; i++) {
			ll tmp = convertBase(b, i);
			if(isPrime(tmp)) {
				ok = 0;
				break;
			}
		}
		if(ok) {
			//print
			for(int i = 0; i < MAXN; i++) {
				printf("%d", b[i]);
			}
			for(int i = 2; i <= ROOT; i++) {
				ll tmp = convertBase(b, i);
				int f = findFirstPrimeFactor(tmp);
				printf(" %d", f);
			}

			printf("\n");
		}

		cnt += ok;
		if(cnt == MAXJ) break;
		nextBitSet();
	}

	return;

	// //test biggest number
	//  b[0] = b[MAXN - 1] = 1;

	//  for(int i = 0; i < MAXN; i++) b[i] = 1;
	// for(int i = 2; i <= 10; i++) {
	// 	long long tmp = convertBase(b, i);
	// 	cout << tmp << endl;
	// 	cout << MAXSIEVE * MAXSIEVE << endl;
	// 	cout << isPrime(tmp) << endl;
	// }
}

int main () {
	freopen(INP, "r", stdin);
	freopen(OUT, "w", stdout);

	preCal();
	scanf("%d ", &T);
	for(int tt = 1; tt <= T; tt++) {
		scanf("%d %d", &N, &J);

		//cout << "Case #" << tt << ":" << endl;
	}
	return 0;
}