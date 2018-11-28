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

#define N 1100000
long long a[N];
int p, q, r, s, n;

inline long long getmin(long long x, long long y) { return x<y?x:y; }
inline long long getmax(long long x, long long y) { return x>y?x:y; }

void conduct() {
	long long ans, tot, sum, pre, head;
	int i, j;
	scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
	for (i=0; i<n; ++i) a[i]=(((long long)i*(long long)p+(long long)q) % (long long)r + s);
	for (sum=i=0; i<n; ++i) sum+=a[i]; tot=sum;
	for (ans=tot, pre=head=i=j=0; i<n; ++i) {
		for (; j<n && head<sum-head; ++j) { ans=getmin(ans, getmax(pre, sum-head)); head+=a[j]; }
		ans=getmin(ans, getmax(pre, head));
		pre+=a[i]; head-=a[i]; sum-=a[i];
	}
	printf("%.10f\n", (double)(tot-ans)/tot);
}

int main() {
	int time; scanf("%d", &time);
	for (int i=1; i<=time; ++i) {
		printf("Case #%d: ", i);
		conduct();
	}
	return 0;
}
