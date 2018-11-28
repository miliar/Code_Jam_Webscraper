#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

const int size = 7;
int m[size];

void clear(int i) {
	For(j, 0, size) {
		m[j] = 0;
	}
}
string key, word;
int k, l, s;

void rec(string &r) {
	if(r.size() == s) {
		int count = 0;
		For(i, 0, sz(r) - sz(word) + 1) {
			if (word == r.substr(i, sz(word))) {
				count++;
			}
		}
		m[count]++;
	} else {
		For(i, 0, sz(key)) {
			r.pb(key[i]);
			rec(r);
			r.pop_back();
		}
	}
}

int solution(int nTest) {
	cin >> k >> l >> s;
	cin >> key;
	cin >> word;

	string rs;
	rec(rs);

	int need = 0;
	int sum = 0;
	For(i, 0, size) {
		if (m[i] != 0) {
			need = i;
		}
		sum += m[i];
	}
	double res = 0;
	For (i, 0, size) {
		cerr << m[i] << " ";
	} cerr << endl;
	For(i, 0, size) {
		int rest = need - i;
		double p = m[i];
		p /= sum;
		res += p * rest;
	}


	printf("%.7lf\n", res);


	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
