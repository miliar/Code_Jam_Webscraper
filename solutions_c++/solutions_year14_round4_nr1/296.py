#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
using namespace std;

#define N 110000
int a[N];
int n, m;

void conduct() {
	int i, head, tail, ans;
	scanf("%d%d", &n, &m);
	for (i=0; i<n; ++i) scanf("%d", &a[i]);
	sort(a, a+n);
	for (ans=head=0, tail=n-1; head<=tail; --tail, ++ans) {
		if (a[head]+a[tail]<=m) ++head;
	}
	printf("%d\n", ans);
}

int main() {
	int time; scanf("%d", &time);
	for (int i=1; i<=time; ++i) {
		printf("Case #%d: ", i);
		conduct();
	}
	return 0;
}
