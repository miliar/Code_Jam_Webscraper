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

int solution(int nTest) {
	int d;
	scanf("%d", &d);
	int res = inf;
	vector<int> v;
	int mx = 0;
	For(i, 0, d) {
		int t;
		scanf("%d", &t);
		v.pb(t);
		mx = max(mx, t);
	}
	For(i, 1, mx + 1) {
		int add = 0;
		For(j, 0, v.size()) {
			int t = v[j];
			if(t) {
				add += (t + (i - 1)) / i - 1;
			}
		}
		res = min(res, add + i);
	}

	printf("%d\n", res);


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
	
