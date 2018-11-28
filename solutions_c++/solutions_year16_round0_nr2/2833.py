#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long long ll;
char s[110];
int a[110];

void flip(int l, int r) {
	for (int i = l, j = r; i < j; i++, j--) {
		swap(a[i], a[j]);
	}
	for (int i = l; i <= r; i++)
		a[i] = 1 - a[i];
}

int main() {
	int o, cas = 0;
	scanf("%d", &o);
	while (o--) {
		scanf("%s", s);
		int n = strlen(s);
		for (int i = 1; i <= n; i++) {
			if (s[i - 1] == '-')
				a[i] = 0;
			else
				a[i] = 1;
		}
		int r = n;
		int ans  = 0;
		while (r > 0) {
			//cout<<ans<<endl;
			//for (int i = 1; i <= n;i ++) cout<<a[i]; cout<<endl;
			if (a[r] == 1) {
				r--;
			} else if (a[1] == 0) {
				flip(1, r);
				ans++;
				r--;
			} else {
				int k = 1;
				while (a[k + 1] == 1) k++;
				ans++;
				flip(1, k);
			}
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
}