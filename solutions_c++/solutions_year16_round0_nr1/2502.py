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

int getDigits(int n) {
	int res = 0;
	do {
		int a = n % 10;
		res |= 1 << a;
		n /= 10;
	} while(n);

	return res;
}

int solution(int nTest) {
	int n;
	scanf("%d", &n);
	if (n == 0) {
		printf("INSOMNIA\n");
		return 0;
	}
	int res = 0;
	For(i, 1, 1000) {
		int cur = getDigits(n * i);
		res = res | cur;
		if (res == 0x3ff) {
			printf("%d\n", n * i);
			return 0;
		}
	}

	printf("INSOMNIA\n");

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
	
