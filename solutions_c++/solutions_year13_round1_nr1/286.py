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

double pi = acos(-1.);

int solution(int nTest) {
	lint R, T;
	scanf("%lld%lld", &R, &T);
	lint l = 1, r = T + 1;
	while(r - l > 1) {
		lint m = (r + l) / 2;
		double t = 2. * R - 3.;
		t *= m;
		t += 2. * m * (m + 1);
		if(t > T) {
			r = m;
		} else {
			l = m;
		}
	}

	printf("%lld\n", l);

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
	
