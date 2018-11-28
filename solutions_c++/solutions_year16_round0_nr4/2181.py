#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;

int main() {
	int o, cas = 0;
	scanf("%d", &o);
	while (o--) {
		int k, c, s;
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", ++cas);
		for (int i = 1; i <= k; i++)
			printf(" %d", i);
		printf("\n");
	}
}