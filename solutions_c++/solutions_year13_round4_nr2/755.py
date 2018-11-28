/*
ID: oooctav1
PROG: checker
LANG: C++
 */
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

using namespace std;
#define PI 3.1415926535897932384626433832795
#define MOD 1000002013
#define mp make_pair
#define pb push_back
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

// ########################################################################################################


int64_t n;
int64_t p;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////
int main() {
	ios_base::sync_with_stdio(false);
	cout.precision(10);
/////////////////////////////////////////////////////////////////////////////////////////////////////////////
	

	int ttt;cin >> ttt;string ss;getline(cin, ss);
	for (int tt = 1; tt <= ttt; tt++) {
		cin >> n >> p;

		int nn = n-1;
		int64_t nr_loses = 0;
		while(((((int64_t)1) << nn) & (p-1))) {
			nn--;
			nr_loses = ((nr_loses + 1) << 1);
			if (nr_loses > p-1) break;
		}

		if (nr_loses > p-1) nr_loses = p-1;

		int64_t nr_wins = (((int64_t)1) << n);
		int x = 0;
		while (p < (((int64_t)1) << (n-x))) x++;

		nr_wins -= (((int64_t)1) << x);

		cout << "Case #" << tt << ": " << nr_loses << " " << nr_wins << endl;
	}

	return 0;
}
