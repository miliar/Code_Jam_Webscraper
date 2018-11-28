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
		int n; cin >> n;
		vector<string> v(n);
		for (int i = 0; i < n; ++i) cin >> v[i];

		int rez = 0;
		int i0 = 0, i1 = 0;
		while (true) {
			if (i0 >= v[0].size() && i1 >= v[1].size()) {
				break;
			}
			if (i0 >= v[0].size() || i1 >= v[1].size() || v[1][i1] != v[0][i0]) {
				rez = -1;	
				break;
			}
			char cur = v[0][i0];
			int size0 = 0, size1 = 0;
			while (i0 < v[0].size() && v[0][i0] == cur) {
				i0 ++;
				size0++;
			}
			while (i1 < v[1].size() && v[1][i1] == cur) {
				i1 ++;
				size1++;
			}
			//cout << i0 << " " << i1 << endl;
			rez += abs(size1 - size0);
		}
		
		if (rez == -1) {
			printf("Case #%d: Fegla Won\n", tt);
		} else {
			printf("Case #%d: %d\n", tt, rez);
		}
	}

	return 0;
}



















