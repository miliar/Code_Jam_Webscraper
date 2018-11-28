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
	if (b == 0) return b;
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
	cin >> T;
	
	for (int tt = 1; tt <= T; ++tt) {
		int n;
		cin >> n;

		vector<string> zip(n);
		for (int i = 0; i < n; ++i) 	cin >> zip[i];







		bool badForAll = false;
		for (int i = 0; i < n; ++i) {
			bool bla[26];
			for (int k = 0; k < 26; ++k) bla[k] = false;
			for (int j = 0; j < n; ++j) {
				if (j != i) {
					for (int k = 0; k < zip[j].size(); ++k) {
						bla[zip[j][k] -'a'] = true;
					}
				}
			}

			for (int j = 1; j + 1 < zip[i].size(); ++j) {
				if (zip[i][j] != zip[i][0] && zip[i][j] != zip[i][zip[i].size() - 1] && bla[zip[i][j]-'a']) {
					badForAll = true;
					break;
				}
			}
			if (badForAll) break;
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 1; j + 1 < zip[i].size(); ++j) {
				if (zip[i][j] == zip[i][0]) {
					for (int k = 0; k < j; k++)
						if (zip[i][j] != zip[i][k]) badForAll = true;
				}
				if (zip[i][j] == zip[i][zip[i].size() - 1]) {
					for (int k = j+1; k < zip[i].size(); k++)
						if (zip[i][j] != zip[i][k]) badForAll = true;
				}
			}
		}


		if (badForAll) {
			printf("Case #%d: 0\n", tt);
			continue;
		}

		long long mmod = 1000000007;
		long long rez = 0;

		vector<int> nr(n, 0);
		for (int i = 0; i < n; ++i) nr[i] = i;

		bool visit[26];
		do {
			for (int i = 0; i < 26; ++i) visit[i] = false;

			bool good = true;
			for (int i = 0; i < n; ++i) {
				
				if (i > 0 && visit[zip[nr[i]][0] - 'a'] && zip[nr[i]][0] != zip[nr[i-1]][zip[nr[i-1]].size() - 1]) {
					//cout << zip[nr[i]] << " " << zip[nr[i+1]] << endl;
					good = false;
					break;
				}
				visit[zip[nr[i]][0] - 'a'] = true;


				if (visit[zip[nr[i]][zip[nr[i]].size() - 1] - 'a'] && zip[nr[i]][0] != zip[nr[i]][zip[nr[i]].size() - 1]) {
					//cout << zip[nr[i]] << " " << zip[nr[i+1]] << endl;
					good = false;
					break;
				}
				visit[zip[nr[i]][zip[nr[i]].size() - 1] - 'a'] = true;

			}
			rez += ((long long)good);
			if (good && rez >= mmod) {
				rez %= mmod;
			}

		} while ( std::next_permutation(nr.begin(),nr.end()) );	

		printf("Case #%d: %lld\n", tt, rez);
	}

	return 0;
}



















