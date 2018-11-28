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

int ar[26];
int result[10];

void init() {
}

void clear(int i) {
	For(i, 0, 26) {
		ar[i] = 0;
	}
	For (i, 0, 10) {
		result[i] = 0;
	}
}



int solution(int nTest) {
	scanf("%s", buffer);
	string s = buffer;
	For (i, 0, sz(s)) {
		ar[s[i] - 'A']++;
	}
	int t = 0;
	t = ar['Z' - 'A'];
	result[0] = t;
	ar['Z' - 'A'] -= t;
	ar['E' - 'A'] -= t;
	ar['R' - 'A'] -= t;
	ar['O' - 'A'] -= t;

	t = ar['W' - 'A'];
	result[2] = t;
	ar['T' - 'A'] -= t;
	ar['W' - 'A'] -= t;
	ar['O' - 'A'] -= t;

	t = ar['X' - 'A'];
	result[6] = t;
	ar['S' - 'A'] -= t;
	ar['I' - 'A'] -= t;
	ar['X' - 'A'] -= t;

	t = ar['G' - 'A'];
	result[8] = t;
	ar['E' - 'A'] -= t;
	ar['I' - 'A'] -= t;
	ar['G' - 'A'] -= t;
	ar['H' - 'A'] -= t;
	ar['T' - 'A'] -= t;

	t = ar['U' - 'A'];
	result[4] = t;
	ar['F' - 'A'] -= t;
	ar['O' - 'A'] -= t;
	ar['U' - 'A'] -= t;
	ar['R' - 'A'] -= t;

	t = ar['T' - 'A'];
	result[3] = t;
	ar['T' - 'A'] -= t;
	ar['H' - 'A'] -= t;
	ar['R' - 'A'] -= t;
	ar['E' - 'A'] -= t;
	ar['E' - 'A'] -= t;

	t = ar['O' - 'A'];
	result[1] = t;
	ar['O' - 'A'] -= t;
	ar['N' - 'A'] -= t;
	ar['E' - 'A'] -= t;

	t = ar['F' - 'A'];
	result[5] = t;
	ar['F' - 'A'] -= t;
	ar['I' - 'A'] -= t;
	ar['V' - 'A'] -= t;
	ar['E' - 'A'] -= t;

	t = ar['S' - 'A'];
	result[7] = t;
	ar['S' - 'A'] -= t;
	ar['E' - 'A'] -= t;
	ar['V' - 'A'] -= t;
	ar['E' - 'A'] -= t;
	ar['N' - 'A'] -= t;

	t = ar['I' - 'A'];
	result[9] = t;
	ar['N' - 'A'] -= t;
	ar['I' - 'A'] -= t;
	ar['N' - 'A'] -= t;
	ar['E' - 'A'] -= t;

	For (i, 0, 10) {
		For (j, 0, result[i]) {
			printf("%d", i);
		}
	}
	printf("\n");



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
	
