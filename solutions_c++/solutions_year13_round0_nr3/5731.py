#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;

bool check(int n) {
	char str[100];
	sprintf(str, "%d", n);
	int j = strlen(str) - 1;
	for(int k = 0; k < j; ++k, --j){
		if(str[k] != str[j]){
			return false;
		}
	}
	return true;
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t){
		int a, b, cnt = 0;
		scanf("%d %d", &a, &b);
		for(int i = a; i <= b; ++i){
			int j = (int)sqrt(i);
			for(int k = j - 1; k <= j + 1; ++k){
				if(k * k == i){
					if(check(k) && check(i)){
						++cnt;
					}
				}
			}
		}
		printf("Case #%d: %d\n", t, cnt);
	}
	return 0;
}
