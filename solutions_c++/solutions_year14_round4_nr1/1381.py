#pragma warning(disable:4996)
#include<stdio.h>
#include<algorithm>
using namespace std;
int TC,T, n, X, w[10010];
int main()
{
	int i, pv, t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TC);
	for (T = 1; T <= TC; T++){
		printf("Case #%d: ", T);
		scanf("%d%d", &n,&X);
		for (i = 0; i < n; i++)scanf("%d", &w[i]);
		sort(w, w + n);
		pv = n - 1;
		t = n;
		for (i = 0; i < n; i++){
			while (w[pv] + w[i] > X)pv--;
			t--;
			if (t > pv) t = pv;
			if (t <= i)break;
		}
		printf("%d\n", n - i);
	}
}