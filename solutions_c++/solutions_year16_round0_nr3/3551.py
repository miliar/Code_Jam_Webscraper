#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
typedef unsigned int u32;
typedef unsigned long long u64;
using namespace std;
const int N=1000;
int T,n,tot;
int pr[N+5],pn=0,a[15];

int check(u64 x) {
	for (int i=1;i<=pn&&pr[i]<x;i++)
		if (x%pr[i]==0)
			return pr[i];
	return 0;
}

void init() {
	for (int i=2;pn<N;i++) {
		bool f=true;
		for (int j=1;j<=pn&&f;j++)
			if (i%pr[j]==0) f=false;
		if (f) pr[++pn]=i;
	}
}

int main() {
	//freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>T;
	cin>>n>>tot;
	init();
	puts("Case #1:");
	for (u32 i=0;i<(1u<<n)-1&&tot>0;i++) {
		if ((i&1)==0||(i>>(n-1)&1)==0) continue;
		bool f=true;
		for (int j=2;j<=10&&f;j++) {
			u64 y=0;
			for (int k=n-1;k>=0;k--)
				y=y*j+(i>>k&1);
			a[j]=check(y);
			if (!a[j]) f=false;
		}
		if (f) {
			--tot;
			for (int j=n-1;j>=0;j--)
				putchar((i>>j&1)?'1':'0');
			for (int j=2;j<=10;j++)
				printf(" %d",a[j]);
			puts("");
		}
	}
	if (tot>0) while(1);
	return 0;
}
