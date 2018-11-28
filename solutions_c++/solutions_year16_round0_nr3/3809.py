#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int m,n,i,T;

bool t[40];

int a[33],cas;

int b[25][11],d[25];

int c[25]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};

void Next() {
	int k=n-2;
	while (a[k]) {
		a[k]=0;
		k--;
	}
	a[k]=1;
}

bool judge() {
	memset(b,0,sizeof(b));
	for (int k=0;k<n;k++)
		for (int i=2;i<11;i++)
			for (int j=0;j<25;j++)
				b[j][i]=(b[j][i]*i+a[k]) % c[j];
	bool t;
	for (int i=2;i<11;i++) {
		t=false;
		for (int j=0;j<25;j++)
			if (b[j][i]==0) {
				d[i]=c[j];
				t=true;
				break;
			}
		if (! t) return false;
	}
	return true;
}

int main() {

//	freopen("C_large.out","w",stdout);

	scanf("%d",&T);
	while (T--) {
		cas++;
		scanf("%d %d",&n,&m);
		memset(a,0,sizeof(a));
		a[0]=1;a[n-1]=1;
		printf("Case #%d:\n",cas);
		while (m--) {
			while (! judge()) Next();
			for (i=0;i<n;i++) printf("%d",a[i]);
			for (i=2;i<11;i++) printf(" %d",d[i]);
			printf("\n");
			Next();
		}
	}
	return 0;
}
