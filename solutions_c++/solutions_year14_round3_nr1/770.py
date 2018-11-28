#include <cstdio>
#include <cstring>
#include <iostream>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define debug 0

#define pb push_back
#define mp make_pair

#define For(i, a, b) for(int i = a; i < b; i++)

#define sz(a) ((int)a.size())

typedef long long lint;


const int inf = 0x7fffffff;
const int Size = 1000 * 1000 * 10;
char buffer[Size];

void clear() {
}

lint gcd(lint a, lint b) {
	if(b) {
		return gcd(b, a % b);
	}
	return a;
}

set<lint> powers;

const char impossible[] = "impossible";

int solution(int nTest) {
	lint k = 1;
	powers.insert(k);
	For(i, 1, 41) {
		k *= 2;
		powers.insert(k);
	}
	lint p, q;
	char c;
	cin >> p >> c >> q;
	lint g = gcd(p, q);
	p /= g;
	q /= g;
	if(powers.count(q) ==0) {
		puts(impossible);
		return 0;
	}
	int res = -1;
	for(int m = 0; m <= 40; m++) {
		if(p >= q) {
			res = m;
			break;
		}
		p *= 2;
	}
	if(res == -1) {
		puts(impossible);
		return 0;
	}
	cout << res << endl;

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		solution(i);
		clear();
	}

	return 0;
}


