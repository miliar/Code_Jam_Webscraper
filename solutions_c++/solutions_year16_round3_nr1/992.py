#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int n, a[100], b[100];

bool cmp(int x, int y) {
	return (a[x]>=a[y]);
}

int main () {
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int TT;
	cin>>TT;
	for (int T=1; T<=TT; ++T) {
		
		cin>>n;
		for (int i=0; i<n; ++i) {
			cin>>a[i];
			b[i]=i;
		}
		printf("Case #%d:", T);
		for (int i=0; i<n-1; ++i)
		  for (int j=i+1; j<n; ++j)
		     if (a[b[i]]<a[b[j]])
		        swap(b[i],b[j]);
		while (a[b[0]]>0) {
			if (a[b[0]]==2&&a[b[1]]==1&&(n==2||a[b[2]]==0)) {
				printf(" %c", b[0]+'A');
				--a[b[0]];
				continue;
			}
			if (n>2 && a[b[0]]==1 && a[b[1]]==1 && a[b[2]]==1 && (n==3 || a[b[3]]==0)) {
				printf(" %c", b[2]+'A');
				--a[b[2]];
				continue;
			}
			printf(" %c", b[0]+'A');
			--a[b[0]];
			if (a[b[0]]==0&&a[b[1]]==0) continue;
			if (a[b[1]]==0) {
				printf("%c", b[0]+'A');
				--a[b[0]];
				continue;
			}
			printf("%c", b[1]+'A');
			--a[b[1]];
			int p=2;
			while (p<n && a[b[p]]>a[b[p-1]]) {
				swap(b[p], b[p-1]);
				++p;
			}
			p=1;
			while (p<n && a[b[p]]>a[b[p-1]]) {
				swap(b[p], b[p-1]);
				++p;
			}
		}
		printf("\n");
	}
}
