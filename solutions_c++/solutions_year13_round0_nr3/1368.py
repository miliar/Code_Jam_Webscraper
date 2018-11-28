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

#define debug 0

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


vector<lint> v;

int isPal(lint i) {
	vector<int> v;
	do {
		v.pb(i % 10);
		i /= 10;
	} while(i);
	int n = sz(v);
	For(i, 0, n) {
		if(v[i] != v[n - 1 - i]) {
			return 0;
		}
	}
	return 1;
}

void init() {
	for(lint i = 1; i <= 10 * 1000 * 1000; i++) {
		if(isPal(i)) {
			if(isPal(i * i)) {
				v.pb(i * i);
			}
		}
	}
	For(i, 0, sz(v)) {
		cerr << v[i] << endl;
	}
}

void clear(int i) {
}

int solution(int nTest) {
	lint a, b;
	cin >> a >> b;
	int u = upper_bound(all(v), b) - v.begin();
	int d = lower_bound(all(v), a) - v.begin();
	printf("%d\n", u - d);


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
	
