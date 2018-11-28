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

void clear(int i) {

}

bool check(int a, int b, int ca, int cb) {
	return (a == ca && b == cb) || (a == cb && b == ca);
}

bool win(int x, int r, int c) {
	if((r * c) % x != 0) {
		return false;
	}

	if(x == 1) {
		return true;
	}

	if(x == 2) {
		return true;
	}

	if(x == 3) {
		return check(r, c, 2, 3) || check(r, c, 3, 3) || check(r, c, 4, 3);
	}
	if(x == 4) {
		return check(r, c, 3, 4) || check(r, c, 4, 4);
	}
	return false;
}

int solution(int nTest) {
	int x, r, c;
	scanf("%d%d%d", &x, &r, &c);

	if(win(x, r, c)) {
		puts("GABRIEL");
	} else {
		puts("RICHARD");
	}

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
	
