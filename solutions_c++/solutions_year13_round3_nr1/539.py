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

#define MAX 1024000

int n, l;
char str[MAX];

void reset() {

}

void read_input() {
	scanf("%s %d", str, &n);
	l = strlen(str);
}

bool is_consonant(int i) {
	if(str[i] == 'a')return false;
	if(str[i] == 'e')return false;
	if(str[i] == 'i')return false;
	if(str[i] == 'o')return false;
	if(str[i] == 'u')return false;
	return true;
}

long long find_ans() {
	read_input();

	long long ans = 0;
	int last = 0;

	int count = 0;
	for(; last < l; last++) {
		if(is_consonant(last)) {
			count++;
		} else {
			count = 0;
		}
		if(count == n)break;
	}
	if(last == l)return 0;

	REP(i, l) {
		ans += (l - last);
		if(i > last - n && is_consonant(i)) {
			count--;
			for(last++; last < l; last++) {
				if(is_consonant(last)) {
					count++;
				} else {
					count = 0;
				}
				if(count == n)break;
			}
			if(last == l)break;
		}
	}

	return ans;
}

int main() {
	int i, c;

	scanf("%d", &c);
	for(i = 1; i <= c; i++) {
		printf("Case #%d: ", i);
		printf("%lld", find_ans());
		printf("\n");
	}

	return 0;
}
