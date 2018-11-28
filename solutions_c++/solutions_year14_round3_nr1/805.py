#include <iostream> 
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <stack>
#include <stdlib.h>
#include <sstream>
#include <stdio.h>
#include <cstring>

using namespace std;
#define PI 3.1415926535897932384626433832795
#define MOD 1000002013
#define mp make_pair
#define pb push_back
#define INF 0x3f3f3f3f

double atof(string s) {
	stringstream ss; ss << s;
	double rez;
	ss >> rez;
	return rez;
}
string ftoa(double d) {
	stringstream ss;
	ss << d;
	return ss.str();
}
int atoi(string s) {
	stringstream ss; ss << s;
	int rez;
	ss >> rez;
	return rez;
}
string itoa(int d) {
	stringstream ss;
	ss << d;
	return ss.str();
}

bool primes[1000001];

void generate_primes() {
	for (int i = 0; i < 1000001; i++) primes[i] = true;
	for (int i = 2; i < 1001; i++) 
		if(primes[i]) 
			for (int j = i*i; j < 1000001; j+= i)
				primes[j] = false;
}

int64_t mod(int64_t x, int64_t p) {
	while(x < 0) x += p;
	return x%p;
}

pair<int64_t,int64_t> euclid(int64_t p, int64_t x) {
	if (x == 0) return mp(1,0);
	pair<int64_t,int64_t> q = euclid(x, p%x);
	return mp(q.second, q.first - q.second * ((int64_t)(p/x))); 
}

int64_t inverted(int64_t x, int64_t p) {
	x = mod(x,p);
	if (x == 1 || x == p-1) return x;
	
	pair<int64_t,int64_t> q = euclid(p,x);
	return mod(q.second, p);
}

long long gcd(long long a, long long b) {
	if (a < b) swap(a,b);
	if (b == 0) return a;
	while (b > 0) {
		long long aux = a%b;
		a = b;
		b = aux;
	} 
	return a;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main() {
	ios_base::sync_with_stdio(false);
	cout.precision(10);
	int MAX_INT = 0x3f3f3f3f;
	long long MAX_LONG_LONG = 0x3f3f3f3f3f3f3f3f;

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
//    freopen("IO/D/input.txt", "r", stdin);
//    freopen("fact.out", "w", stdout);

/*
	string line;
	getline(cin, line);
*/


	string line;
	int T;
	scanf("%d", &T);	
	
	for (int tt = 1; tt <= T; ++tt) {
		long long p, q; 
		scanf("%lld/%lld", &p, &q);

		long long g = gcd(p,q);
		p = p/g;
		q = q/g;

		long long power = 1;
		while (power < q) power = (power << 1);

		if (power != q || p == 0) {
			printf("Case #%d: impossible\n", tt);
		} else {
			int nrgen = 0;
			while (p < q) {
				nrgen ++;
				q = (q >> 1);
			}



			
			printf("Case #%d: %d\n", tt, nrgen);
		}
	}

	return 0;
}



















