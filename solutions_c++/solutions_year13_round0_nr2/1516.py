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


const int size = 101;
int ar[size][size];
int gr[size][size];

void clear() {
	For(i, 0, size) {
		For(j, 0, size) {
			ar[i][j] = 0;
			gr[i][j] = inf;
		}
	}
}

int solution(int nTest) {
	int n, m;
	scanf("%d%d", &n, &m);
	For(i, 0, n) {
		For(j, 0, m) {
			scanf("%d", &ar[i][j]);
		}
	}
	For(i, 0, n) {
		int mx = 0;
		For(j, 0, m) {
			mx = max(mx, ar[i][j]);
		}
		For(j, 0, m) {
			gr[i][j] = min(gr[i][j], mx);
		}
	}
	For(j, 0, m) {
		int mx = 0;
		For(i, 0, n) {
			mx = max(mx, ar[i][j]);
		}
		For(i, 0, n) {
			gr[i][j] = min(gr[i][j], mx);
		}
	}
	For(i, 0, n) {
		For(j, 0, m) {
			if(ar[i][j] != gr[i][j]) {
				puts("NO");
				return 0;
			}
		}
	}
	puts("YES");


	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear();
		solution(i);
	}

	return 0;
}
	
