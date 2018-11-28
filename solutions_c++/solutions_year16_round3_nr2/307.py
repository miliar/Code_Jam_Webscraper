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

const int size = 51;
int ar[size][size];

void init() {
	For (i, 1, size) {
		For (j, i + 1, size) {
			ar[i][j] = 1;
		}
	}
}

void clear(int i) {
	For (i, 0, size) {
		ar[i][0] = 0;
		ar[0][i] = 0;
	}
}

int solution(int nTest) {
	lint b; lint m;
	scanf("%lld", &b);
	scanf("%lld", &m);
//	cerr << b <<  " " << m << endl;
	ar[0][b - 1] = 1;
	m--;
	lint t = m;
	For (i, 0, b - 2) {
		lint s = i;
		lint a = 1;
		if (m & (a << s)) {
			ar[0][b - (i + 2)] = 1;
			t -= a << s;
		}
//		cerr << i << ":" <<  t << ":" << (1 << s) << endl;
	}
	if (t == 0) {
		puts("POSSIBLE");
		For (i, 0, b) {
			For (j, 0, b) {
				printf("%d", ar[i][j]);
			}
			printf("\n");
		}
	} else {
		puts("IMPOSSIBLE");
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
	
