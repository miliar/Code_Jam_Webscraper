// Lupus Nocawy 2016
// Code Jam 2016
// https://code.google.com/codejam
// https://code.google.com/codejam/contest/6254486/dashboard
// Problem C. Coin Jam

#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cmath>
using namespace std;
#define REP(i,n) for(int i=0, _n=n; i<_n; ++i)
#define FOR(i,a,b) for(int i=(a), _b=(b); i<=_b; ++i)
#define FORD(i,a,b) for(int i=(a), _b=(b); i>=_b; --i)
#define IT(i,x) __typeof__(x) i=x
#define FOREACH(it,x) for(__typeof__((x).begin()) it=(x).begin(); it!=(x).end(); ++it)
#define ALL(x) x.begin(),x.end()
#define MP make_pair
#define PB push_back
#define DEBUG(x) if(debug) cout << x << endl;
typedef unsigned int uint;
typedef long long int lli;
typedef unsigned long long int llu;
typedef pair<int,int> pii;
const int debug=0;

const int INF = 2147483647;
const int max_n = 2147483647;
const uint max_un = 4294967295;

vector<int> prime;

bool isPrime(llu n){
	int i=1;
	llu p = prime[i];
	while(p*p <= n){
		if(n%p==0)
			return 0;
		++i;
		p = prime[i];
	}
	return 1;
}

void findAllPrimes(void){
	prime.PB(1);
	prime.PB(2);
	prime.PB(3);
	prime.PB(5);
	int p=7;
	while(p<=65537){
		if(isPrime(p))
			prime.PB(p);
		p+=2;
	}
}

void itb(llu n, vector<int> &m){
	m.clear();
	while(n>0){
		m.PB(n%2);
		n/=2;
	}
}

llu convert(vector<int> &m, int base){
	llu n = 0;
	llu b = 1;
	REP(i,m.size()){
		n += m[i]*b;
		b *= base;
	}
	return n;
}

int factor(llu n){
	unsigned int i=1;
	llu p = prime[i];
	while(p*p <= n){
		if(n%p==0)
			return p;
		++i;
		if(i>=prime.size())
			return 0;
		p = prime[i];
	}
	return 0;
}

llu fctr[11];

bool isJamCoin(vector<int> &m){
	FOR(base,2,10){
		llu n = convert(m,base);
		//printf("%llu\n", n);
		fctr[base] = factor(n);
		if(fctr[base]==0)
			return 0;
	}
	return 1;
}

int main(void){
	findAllPrimes();
	printf("Case #1:\n");
	int t, n, j;
	scanf("%d %d %d ", &t, &n, &j);
	llu jamcoin = 1;
	vector<int> jamcoinb;
	REP(i,n-1)
		jamcoin <<= 1;
	jamcoin++;
	itb(jamcoin,jamcoinb);
	//FORD(i,jamcoinb.size()-1,0) 
		//printf("%d", jamcoinb[i]);
	//printf("\n");
	while(j){
		if(isJamCoin(jamcoinb)){
			j--;
			FORD(i,jamcoinb.size()-1,0) 
				printf("%d", jamcoinb[i]);
			printf(" ");
			FOR(i,2,10){
				printf("%llu ", fctr[i]);
			}
			printf("\n");
		}
		jamcoin+=2;
		itb(jamcoin,jamcoinb);
	}
	return 0;
}
