#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define REP(i, n) for(int i = 0; i < (n); i++)
#define FOR(i, x, y) for(int i = (x); i <= (y); i++)
#define RFOR(i, x, y) for(int i = (x); i >= (y); i--)

#define REMIN(x, y) x = (x < (y)) ? x : (y)
#define REMAX(x, y) x = (x > (y)) ? x : (y)

//#define DEBUG

#ifndef DEBUG
#define ISDEBUG false
#define PRINT(x)
#else
#define ISDEBUG true
#define PRINT(x) cout << #x << ": " << x << endl
#endif
#define IFDEBUG() if(ISDEBUG)

using namespace std;

#define MAX 10240000LL
#define MAXS 1024

long long cache[MAX], _pow[MAX];

void reset() {

}

bool is_palindrome(long long l) {
	char str[MAXS];
	int len = sprintf(str, "%lld", l);
	for(int i = 0, j = len - 1; i < j; i++, j--) {
		if(str[i] != str[j])return false;
	}
	return true;
}

void init() {
	long long count = 0;
	for(long long i = 1; i < MAX; i++) {
		cache[i] = count;
		_pow[i] = i * i;
		if(!is_palindrome(i))continue;
		if(!is_palindrome(_pow[i]))continue;
		cache[i] = ++count;
	}
}

long long ceil_sqrt(long long l) {
	long long lb = 0, ub = MAX - 1, mid;
	while(lb < ub) {
		mid = (lb + ub) / 2;
		if(_pow[mid] == l) {
			return mid;
		} else if(_pow[mid] < l) {
			lb = mid + 1;
		} else {
			if(ub == mid) {
				return lb;
			}
			ub = mid;
		}
	}
	return ub;
}

long long floor_sqrt(long long l) {
	long long lb = 0, ub = MAX - 1, mid;
	while(lb < ub) {
		mid = (lb + ub + 1) / 2;
		if(_pow[mid] == l) {
			return mid;
		} else if(_pow[mid] < l) {
			if(lb == mid) {
				return lb;
			}
			lb = mid;
		} else {
			ub = mid - 1;
		}
	}
	return lb;
}

void read_input() {
}

long long find_ans() {
	read_input();

	long long a, b;
	scanf("%lld %lld", &a, &b);
	return cache[floor_sqrt(b)] - cache[floor_sqrt(a - 1)];
}

int main() {
	int i, c;

	init();
	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		printf("%lld", find_ans());
		printf("\n");
	}

	return 0;
}
