#include <iostream>
#include <vector>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fornn(i, a, b) for (int i = (int)(a); i < (int)(b); ++i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<int>::iterator vi_it;
typedef vector<vi> vvi;

typedef long long i64;
typedef pair<i64, i64> pi64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
int N = 32;
int L = 50;
int T;
string s;
int num;
int limit = 10000000;
long big[9];
vector<int> primes(limit,0);
vector<vector<int> > resi;

long pow(int base, int p) {
	if (p == 1) return base;
	long a = pow(base, p/2);
	if (p % 2 == 0) return a*a;
	return a*a*base;
}


int getprimes(){
	vector<int> a(limit,0);
	int p = 0;
	for (int i = 2; i< limit;++i) {
		if (a[i] == 0) {
			for (int j = 2*i; j < limit; j+=i) {
				a[j] = 1;
			}
			primes[p++] = i;
		}
	}
	primes.resize(p);
	if (N == 32) {
		resi.resize(9, vector<int>(p));
		for (int j = 2; j<=10;++j) {
			long pa;
			for (int i = 0; i < p; ++i) {
				int prime = primes[i];
				int res;
				pa = pow(j, 8);
				res = 1;
				for (int k = 0; k<3;++k) {
					res = (res*pa)%prime;	
				}
				pa = pow(j, 7);
				res = (res*pa)%prime;	
				resi[j-2][i] = res;
			}
		}
	}
    return 0;
}

int isprime(long val, int base) {
	for (int i = 0; i < primes.size(); ++i) {
		long add;
		if (N == 32) {
			add = resi[base-2][i];	
		} else {
			add = big[base-2];
		}
		if (primes[i] >= (val+add)) {
			break;
		}
		if ((val + add) % primes[i] == 0) {
			return primes[i];
		}
	}
	return 0;
}
long convert(unsigned int from, int base); 

void cal() {
	if (N<=16){
	for (int i=0;i<9;++i) {
		big[i] = pow(i+2, N-1);
	}
	}
	int p = 0;
	unsigned int B = (1<<(N-1)) - 1;
	unsigned int A = 1;
	unsigned int tempa;
	for (unsigned int a = A; a <= B && p < L; a+=2) {
		int u[9];
		if (0 == (u[0]=isprime(a, 2))) {
			goto cont;
		}
		for (int base = 3; base <= 10; base++) {
			if (0 == (u[base-2] = isprime(convert(a, base), base))) {
				goto cont;
			}
		}
		p++;
		char s[N+1];
		s[N] = 0;
		s[0] = '1';
		tempa = a;
		for (int i = 0;i<N-1;++i) {
			s[N-1-i] = (tempa&1)+'0';
			tempa >>= 1;
		}
		printf("%s", s);
		for (int i=0;i<9;++i) {
		printf(" %d", u[i]);
		}
		printf("\n");
cont:
		continue;
	}
	fprintf(stderr,"number of good number %d\n", p);
}
long convert(unsigned int from, int base) {
	long to = 0;
	long add = 1;
	for (int i = 0; i < 32; ++i) {
		if (from & 1) {
			to += add;
		}	
		from >>= 1;
		add *= base;
	}
	return to;
}


int main(int argc, char* argv[]){
	cin >> T;
	cin >> N >> L;
	printf("Case #1:\n");
	getprimes();
	cal();
    return 0;
}
