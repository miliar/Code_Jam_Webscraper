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
//////////////////////////////////////////////////////////////////////////////////////////////////////////////

int main() {
	ios_base::sync_with_stdio(false);
	cout.precision(10);

/////////////////////////////////////////////////////////////////////////////////////////////////////////////
//    freopen("IO/D/input.txt", "r", stdin);

//    freopen("fact.out", "w", stdout);

/*
	string line;
	getline(cin, line);
*/

	string line;
	int T;
	cin >> T;
	
	for (int tt = 1; tt <= T; ++tt) {
		double c,f,x;
		cin >> c >> f >> x;

		int k = 0;
		for (;;k++) {
			if ((x-c) * (2 + f * (k+1)) <= x * (2 + k*f)) {
				break;
			}
		}

		double rez = 0;
		for (int i = 0; i < k; ++i) {
			rez += c/(2.0 + i*f);
		}

		rez += x/(2 + k*f);
		printf("Case #%d: %.7lf\n", tt, rez);
	}

	return 0;
}



















