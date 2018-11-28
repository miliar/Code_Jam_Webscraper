#include <bits/stdc++.h>
using namespace std;

const int MAX_D = 1001, MAX_P = 1001;

int z, n, res, pan[MAX_D];

int main() {
	scanf("%d", &z);
	for(int c = 1; c <= z; c++) {
		res = MAX_P;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
			scanf("%d", &pan[i]);
		sort(pan, pan+n, greater<int>());
		for(int i = 1; i <= pan[0]; i++) {
			int cnt = 0;
			for(int j = 0; j < n && pan[j]>i; j++)
				cnt+=(pan[j]/i)+((pan[j]%i)>0)-1;
			res = min(res, i+cnt);
		}
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}
