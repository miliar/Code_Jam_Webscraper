#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	scanf("%d",&T);
	for (int z=1;z<=T;++z) {
		int n;
		scanf("%d ",&n);
		int skrg=0;
		int jwb=0;
		for (int i=0;i<n+1;++i) {
			char c;
			scanf("%c",&c);
			int d=c-'0';
			if (skrg<i) {
				jwb+=i-skrg;
				skrg=i;
			}
			skrg+=d;
		}
		printf("Case #%d: %d\n",z,jwb);
	}
	return 0;
}
