#define _CRT_SECURE_NO_DEPRECATE

#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for(int i=a; i<=b; i++)
#define fj(a, b) for(int j=a; j<=b; j++)
#define fo(a, b) for(int o=a; o<=b; o++)
#define fdi(a, b) for(int i=a; i>=b; i--)
#define fdj(a, b) for(int j=a; j>=b; j--)
#define fdo(a, b) for(int o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x))
#define COPY(x,y) memcpy(x, y, sizeof(y))
#define LEN(x) (int)x.length()
#define SIZE(x) (int)x.size()

typedef long long int64;

int number_of_tests;
int test_number;

int n, r, p, s;

void read() {
	scanf("%d %d %d %d", &n, &r, &p, &s);
}

int compare(char a, char b) {
	if (a == b) return 0;
	if (a == 'S' && b == 'P') return 1;
	if (a == 'P' && b == 'R') return 1;
	if (a == 'R' && b == 'S') return 1;
	return -compare(b, a);
}

bool go(string s) {
	while (LEN(s) > 1) {
		string g;
		for (int i = 0; i < LEN(s); i += 2) {
			int t = compare(s[i], s[i + 1]);
			if (t == 0) return false;
			if (t == 1) {
				g += s[i];
			} else {
				g += s[i + 1];
			}
		}
		s = g;
	}
	return true;
}

void solve() {
	string str;
	fi(1, p) {
		str += "P";
	}
	fi(1, r) {
		str += "R";
	}
	fi(1, s) {
		str += "S";
	}
	do {
		if (go(str)) {
			printf("%s\n", str.c_str());
			return;
		}
	} while (next_permutation(str.begin(), str.end()));
	printf("IMPOSSIBLE\n");
}

int main(int argc, char **argv) {
	if (argc == 1) {
		freopen("input.txt","r",stdin);
	} else {
		freopen(argv[1], "r",stdin);
	}
	freopen("output.txt","w",stdout);
	scanf("%d", &number_of_tests);
	for (test_number = 1; test_number <= number_of_tests; test_number++) {
		read();
		printf("Case #%d: ", test_number);
		solve();
		fflush(stdout);
	}
	return 0;
}
