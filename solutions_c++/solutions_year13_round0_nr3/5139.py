#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cmath>
using namespace std;
#define REP(i, n) for (int i = 0; i < n; ++i)
#define TR(i, x) for (typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define PB push_back
#define MP make_pair
typedef long long ll;

const ll MOD = 1e9 + 7;
const int MAXK = 10;
const int MAXN = 1e7 + 1e3;
int mycount[MAXN];
ll n, m;

bool isPalindrome(ll x) {
	int digits[20];
	int cnt = 0;
	while (x > 0) {
		digits[cnt++] = x % 10;
		x /= 10;
	}
	for (int i = 0; i < cnt / 2; ++i)
	if (digits[i] != digits[cnt - i - 1])
		return false;
	return true;
}
bool check(ll x) {
	return isPalindrome(x) && isPalindrome(x * x);
}
void prepare() {
	mycount[0] = 0;
	for (int i = 1; i <= MAXN; ++i) {
		mycount[i] = mycount[i-1] + check(i);
	}
}

int main() {
	prepare();
	int test;
	cin >> test;
	for (int cas = 1; cas <= test; ++cas) {
		cin >> n >> m;
		ll sqrt_m = (ll)sqrt(m);
		ll sqrt_n = (ll)sqrt(n-1);
		printf("Case #%d: ",cas);
		cout << mycount[sqrt_m] - mycount[sqrt_n] << endl;
	}
}

