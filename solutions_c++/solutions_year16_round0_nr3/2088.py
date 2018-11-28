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

//const int N = 16;
//const int J = 50;
//const int N = 6;
//const int J = 300;
const int N = 32;
const int J = 500;

int r9[N][11];
int isOdd[N][11];
int lastNumber[N][11];

int get9(int a) {
	if (a == 0) {
		return 0;
	}
	if (a % 9 == 0) {
		return 9;
	}
	return a % 9;
}

void init() {
	For (i, 2, 11) {
		int a = 1;
		int b = 1;
		For(j, 0, N) {
			r9[j][i] = a;
			a *= i;
			a = get9(a);
			isOdd[j][i] = 1 & i;
			lastNumber[j][i] = b;
			b *= i;
			b %= 10;
		}
		isOdd[0][i] = 1;
	}
	/*
	For (i, 2, 11) {
		printf("%d:", i);
		For(j, 0, N) {
			printf(" %d", r9[j][i]);
		}
		puts("");
	}
	*/

}

void clear(int i) {

}


int solution(int nTest) {
	int total = 0;
	For (i, 0, 1 << (N - 2)) {
		vector<int> res;
		For (j, 2, 11) {
			int r = r9[0][j] + r9[N-1][j];
			int r2 = isOdd[0][j] + isOdd[N-1][j];
			int r3 = lastNumber[0][j] + lastNumber[N-1][j];
			int c = 1;
			int temp = i;
			int sum = 0;
			while (temp) {
				r += (temp & 1) * r9[c][j];
				r2 += (temp & 1) * isOdd[c][j];
				r3 += (temp & 1) * lastNumber[c][j];
				sum += (temp & 1) * ((c & 1) ? -1 : 1);
				c++;

				temp >>= 1;
			}
			int root = get9(r);
			r3 %= 10;
			if (root == 9 || root == 3 || root == 6) {
				res.pb(3);
			} else if ((r2 & 1) == 0) {
				res.pb(2);
			} else if (r3 == 5 || r3 == 0) {
				res.pb(5);
			} else if (j == 10 && (sum % 11 == 0)) {
				res.pb(11);
			} else {
				break;
			}
		}
		if (sz(res) == 9) {
			printf("1");
			for (int k = N - 3; k >= 0; k--) {
				printf("%d", (i >> k) & 1);
			}
			printf("1");
			For(i, 0, sz(res)) {
				printf(" %d", res[i]);
			}
			puts("");
			total++;
			if (total == J) {
				return 0;
			}

		}
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
		printf("Case #%d:\n", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
