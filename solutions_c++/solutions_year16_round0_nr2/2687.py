#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>
#include <map>
#include <iostream>
using namespace std;

typedef long long ll;
char str[123];
int main() {
	freopen("B-large.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	for(int cas = 1; cas <= T; cas ++) {
		scanf("%s", str);
		int ans = 0;
		int n = strlen(str);
		for(int i = 1; i < n; i ++) ans += str[i] != str[i - 1];
		ans += str[n - 1] == '-';
		printf("Case #%d: ", cas);
		printf("%d\n", ans);
	}
}
