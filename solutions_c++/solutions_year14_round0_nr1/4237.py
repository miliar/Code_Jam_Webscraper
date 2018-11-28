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
		int nr1; cin >> nr1;
		set<int> set1;
		getline(cin, line);
		for (int i = 1; i <= 4; ++i) {
			getline(cin, line);
//			printf("%s\n", line.c_str());
			if (i == nr1) {
				stringstream ss;
				ss << line;
				for (int j = 0; j < 4; ++j) {
					int k;
					ss >> k;
					set1.insert(k);
				}
			}
		}

		int nrcommon = 0;
		int that = -1;
		int nr2; cin >> nr2;
		getline(cin, line);
		for (int i = 1; i <= 4; ++i) {
			getline(cin, line);
			if (i == nr2) {
				stringstream ss;
				ss << line;
				for (int j = 0; j < 4; ++j) {
					int k;
					ss >> k;
					if (set1.find(k) != set1.end()) {
						that = k;
						nrcommon++;
					}
				}
			}
		}		

		if (nrcommon == 0) {	
			printf("Case #%d: Volunteer cheated!\n", tt);
		} else if(nrcommon > 1) {
			printf("Case #%d: Bad magician!\n", tt);
		} else {
			printf("Case #%d: %d\n", tt, that);
		}
	}

	return 0;
}



















