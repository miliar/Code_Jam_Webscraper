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

#define N 1100
int a[N], seq[N], vst[N];
int n;

int cmp(const int &i, const int &j) { return a[i]<a[j]; }
inline int getmin(int x, int y) { return x<y?x:y; }

void conduct() {
	int i, j, k, ans;
	scanf("%d", &n);
	for (i=0; i<n; ++i) scanf("%d", &a[i]);
	for (i=0; i<n; ++i) seq[i]=i; sort(seq, seq+n, cmp);
	memset(vst, 0, sizeof(vst));
	for (ans=i=0; i<n; ++i) {
		for (j=k=0; j<seq[i]; ++j) if (!vst[j]) k++;
		ans+=getmin(k, n-i-1-k);
		vst[seq[i]]=1;
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
