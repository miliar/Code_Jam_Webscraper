#include <iostream>
#include <vector>
#include <stack>
#include <chrono>
#include <cassert>
#include <cmath>
#include <bitset>
#include <unordered_set>
using namespace std;
#define DB(a) << #a " == " << (a) << ";	"
#define REP(n) for (int i = 0; i < int(n); ++i)
#define FOR(i,n) for (int i = 0; i < int(n); ++i)
#define SEG(i,a,b) for (int i = (a); i <= (b); ++i)
#ifdef DBG
#define WR(things_to_wrap) things_to_wrap
int __GOV = 0, __GOVTH = int(1e8);
#define OP {if (++__GOV > __GOVTH) cerr << "exit(1): __GOV exceeded " << __GOVTH << endl, exit(1);}
#else
#define WR(things_to_wrap)
#define OP
#endif
#define CR(text_to_cerr) WR(cerr << "" text_to_cerr << endl;)
#define pb push_back
typedef unsigned long long int ulli;
typedef long double ld;
typedef unsigned int ui;
// const int CNT = 3, JAML = 6;
const int CNT = 50, JAML = 16;
// const int CNT = 500, JAML = 32;
typedef bitset<JAML> jamcoin;
typedef unordered_set<ulli> hset;

const int PCMAX = int(3e6);
ui prime[PCMAX]; int lp;
#define bakname "/mnt/ramdisk/primes.bak"
FILE * bak;

inline void gotcha(ui n){
	prime[++lp] = n;
	fprintf(bak, "%u\n", n);
	fflush(bak);
	if (!(lp % 100000)) {
		cerr << "have generated " << lp << " primes. ";
		system("date");
	}
}

void initprimes(){
	bak = fopen(bakname, "r");
	lp = -1;
	do {
		fscanf(bak, "%u", &prime[++lp]);
	} while (prime[lp] != 0);
	--lp;
	fclose(bak);
	bak = fopen(bakname, "a");
	if (lp == -1) {
		gotcha(3);
		gotcha(5);
		gotcha(7);
	} else {
		--lp;
	}
}

ui ldivisor;
inline bool is_prime(ulli n){
	ldivisor = 0;
	ui stop = sqrt(ld(n))+1;
	bool ans = true;
	for (int i = 0; i <= lp && prime[i] <= stop; ++i)
		if (!(n%prime[i])) {
			ldivisor = prime[i];
			ans = false;
			break;
		}
	return ans;
}

void genprimes(){
	ui stop = ui((1ll << 32)-1);
	// ui stop = 110;
	for (ui n = prime[lp]+2; n <= stop; n += 2) {
		if (is_prime(n))
			gotcha(n);
	}
}

jamcoin gencancoin(){
	jamcoin jc;
	jc.set(0, 1); jc.set(JAML-1, 1);
	SEG(i, 2, JAML-2) jc.set(i, rand()&1);
	return jc;
}

inline ulli interpret(jamcoin jc, int base){
	ulli val = 0, p = 1;
	REP(JAML){
		val += p * jc.test(i);
		p *= base;
	}
	return val;
}

hset ver;
int ansc = 0;
ui divisor[11];
ulli val[11];
void solve(){
	jamcoin jc;

	while (ansc < CNT){
		do {OP
			jc = gencancoin();
		} while (ver.count(jc.to_ullong()) != 0);
		ver.insert(jc.to_ullong());

		bool ok = true;
		for (int b = 10; b >= 2; --b){
			if (is_prime(val[b] = interpret(jc, b))){
				ok = false;
				break;
			}
			divisor[b] = ldivisor;
		}
		if (ok){
			++ansc;
			cout << jc.to_string();
			SEG(b, 2, 10){
				assert(val[b] % divisor[b] == 0);
				cout << " " << divisor[b];
			}
			cout << endl;
		}
		WR(if (__GOV%100 == 0) cerr DB(__GOV) DB(ansc) << endl;)
	}
}

int main(){ // WR(srand(chrono::system_clock::now().time_since_epoch().count());)
	initprimes();
	CR(DB("init complete!"))
	// genprimes();

	cout << "Case #1:" << endl;
	solve();
	return 0;
}
