#include <iostream>
#include <utility>
#include <limits.h>
#include <fstream>
#include <string>
#include <string.h>
#include <queue>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#define INF 987654321
using namespace std;
typedef long long lld;
int check[11];
bool remain();
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	lld tmp;
	int i;
	int module;
	queue<lld> myQ;
	scanf("%d",&t);
	for (int TestCase = 1; TestCase <= t; TestCase++) {
		memset(check, 0, sizeof(check));
		lld n;
		
		scanf("%lld",&n);
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", TestCase);
		}
		else {
			 i = 1;
			do {
				tmp = n*i;
				while (tmp > 0) {
					
					module = tmp % 10;
					check[module] = 1;
					tmp = tmp / 10;
					
				}
				i++;
			} while (remain());
			printf("Case #%d: %lld\n",TestCase, n*(i - 1));
		}
		
	}
	return 0;
}

bool remain() {
	for (int i = 0; i < 10; i++) {
		if (check[i] == 0) {
			return true;
		}
	}
	return false;
}
