#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <climits>
#include <complex>
#include <fstream>
#include <cassert>
#include <cstdio>
#include <bitset>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <cmath>

using namespace std;

typedef unsigned long long ull;
const int maxn = 100000010;
char str[maxn];
int n, j;


ull quickmul(ull x, ull n) {
	ull ans = 1;
	ull t = x;
	while(n) {
		if(n & 1) {
			ans *= t;
		}
		t = t * t;
		n >>= 1;
	}
	return ans;
}

void addone(char* ca) {
	ca[n-1] += 1;
	for(int i = n - 1; i >= 0; i--) {
		if(ca[i] > '1') {
			ca[i] = '0';
			ca[i-1]++;
		}
	}
}

void convert(char* str, int ary, ull& aim) {
	ull k = 1;
	ull p = 1;
	aim = 0;
	for(int i = n - 1; i >= 0; i--) {
		aim = aim + (str[i] - '0') * k;
		k = (ull)quickmul(ary, p++);
	}
}

bool isprime(ull a) {
	ull t = ull(sqrt(a)) + 10;
	for(ull i = 2; i < t; i++) {
		if(a % i == 0) return 0;
	}
	return 1;
}

vector<ull> ans;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int _ = 1; _ <= T; _++) {
		printf("Case #%d:\n", _);
		cin >> n >> j;
		memset(str, 0, sizeof(str));
		for(int i = 0; i < n; i++) {
			str[i] = '0';
		}
		str[0] = '1'; str[n-1] = '1';
	
		ull cnt = 0;
		while(1) {
			if(str[n-1] == '0') {
				addone(str);
				continue;
			}
			if(cnt == j) break;
			// if(strlen(str) > n) break;
			ull aim;
			bool flag = 1;
			ans.clear();
			for(int i = 2; i <= 10; i++) {
				convert(str, i, aim);
				if(isprime(aim) == 1) {
					flag = 0;
					break;
				}
				ans.push_back(aim);
			}
			if(flag) {
				printf("%s ", str);
				for(int i = 0; i < ans.size(); i++) {
					for(int j = 2; j < ans[i]; j++) {
						if(ans[i] % j == 0) {
							printf("%d ", j);
							break;
						}
					}
				}
				printf("\n");
				cnt++;
			}
			addone(str);
		}
	}
	return 0;
}