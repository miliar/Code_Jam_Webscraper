#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
int scan();
int dwar(int n, int nm[1005], int km[1005]);
int war(int n, int nm[1005], int km[1005]);
int cmp(const void*p, const void*q) {
	return *(int*)p - *(int*)q;
}
int main() {
	int T, tc, n;
	for(scanf("%d", &T), tc = 1; tc <= T; tc++) {
		scanf("%d", &n);
		int nm[1005], km[1005];
		for(int i = 0; i < n; i++) nm[i] = scan();
		for(int i = 0; i < n; i++) km[i] = scan();
		qsort(nm, n, sizeof(nm[0]), cmp);
		qsort(km, n, sizeof(km[0]), cmp);
		printf("Case #%d: %d %d\n", tc, dwar(n, nm, km), war(n, nm, km));
	}
	return 0;
}
int scan() {
	int i;
	char s[10];
	scanf("%d.%s", &i, s);
	sscanf(s, "%d", &i);
	return i * pow(10, 5-strlen(s));
}
int dwar(int n, int nm[1005], int km[1005]) {
	int ans = 0;
	for(int i = 0, j = 0; i < n; i++)
		if(nm[i] > km[j]) ans++, j++;
	return ans;
}
int war(int n, int nm[1005], int km[1005]) {
	int ans = 0;
	for(int i = 0, j = 0; i < n; i++) {
		while(nm[i] > km[j] && j < n) j++;
		if(j >= n) ans++;
		else j++;
	}
	return ans;
}
