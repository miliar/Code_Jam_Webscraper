#include <bits/stdc++.h>

using namespace std;

int r,p,s,t,n,i,j,tes,x,y,z;
int a[15][40007];
int b[40007];

void SORT() {
	int i,j,k;
	string nyan;
	for (j=1 ; j<=(1 << n) ; j++) {
		if (a[n][j] == 0) nyan += 'S';
		if (a[n][j] == 1) nyan += 'P';
		if (a[n][j] == 2) nyan += 'R';
	}
	
	for (i=1 ; i<=n ; i++) {
		string tmp = "";
		for (j=1 ; j<=(1 << n) ; j+=(1 << i)) {
			string tmp1 = nyan.substr(j-1,(1 << (i-1)));
			string tmp2 = nyan.substr(j-1+(1 << (i-1)),(1 << (i-1)));
			if (tmp1 < tmp2) tmp = tmp + tmp1 + tmp2; else tmp = tmp + tmp2 + tmp1;
		}
		nyan = tmp;
	}
	
	cout << nyan;
}

int main() {
	scanf("%d",&t);
	while (t--) {
		scanf("%d%d%d%d",&n,&r,&p,&s);
		
		// R = 2
		// P = 1
		// S = 0
		
		a[0][1] = 2;
		for (i=1 ; i<=n ; i++) {
			for (j=1 ; j<=(1 << (i-1)); j++) {
				if (a[i-1][j] == 0) {
					a[i][2*j-1] = 1;
					a[i][2*j] = 0;
				}
				if (a[i-1][j] == 1) {
					a[i][2*j-1] = 1;
					a[i][2*j] = 2;
				}
				if (a[i-1][j] == 2) {
					a[i][2*j-1] = 2;
					a[i][2*j] = 0;
				}
			}
		}
		
		b[0] = 0;
		b[1] = 0;
		b[2] = 0;
		for (j=1 ; j<=(1 << n) ; j++) {
			b[a[n][j]]++;
		}
		
		if (b[0] == s && b[1] == p && b[2] == r) {
			printf("Case #%d: ",++tes);
			SORT();
			printf("\n");
			continue;
		}
		
		a[0][1] = 1;
		for (i=1 ; i<=n ; i++) {
			for (j=1 ; j<=(1 << (i-1)); j++) {
				if (a[i-1][j] == 0) {
					a[i][2*j-1] = 1;
					a[i][2*j] = 0;
				}
				if (a[i-1][j] == 1) {
					a[i][2*j-1] = 1;
					a[i][2*j] = 2;
				}
				if (a[i-1][j] == 2) {
					a[i][2*j-1] = 2;
					a[i][2*j] = 0;
				}
			}
		}
		
		b[0] = 0;
		b[1] = 0;
		b[2] = 0;
		for (j=1 ; j<=(1 << n) ; j++) {
			b[a[n][j]]++;
		}
		
		if (b[0] == s && b[1] == p && b[2] == r) {
			printf("Case #%d: ",++tes);
			SORT();
			printf("\n");
			continue;
		}
		
		a[0][1] = 0;
		for (i=1 ; i<=n ; i++) {
			for (j=1 ; j<=(1 << (i-1)); j++) {
				if (a[i-1][j] == 0) {
					a[i][2*j-1] = 1;
					a[i][2*j] = 0;
				}
				if (a[i-1][j] == 1) {
					a[i][2*j-1] = 1;
					a[i][2*j] = 2;
				}
				if (a[i-1][j] == 2) {
					a[i][2*j-1] = 2;
					a[i][2*j] = 0;
				}
			}
		}
		
		b[0] = 0;
		b[1] = 0;
		b[2] = 0;
		for (j=1 ; j<=(1 << n) ; j++) {
			b[a[n][j]]++;
		}
		
		if (b[0] == s && b[1] == p && b[2] == r) {
			printf("Case #%d: ",++tes);
			SORT();
			printf("\n");
			continue;
		}
		
		printf("Case #%d: IMPOSSIBLE\n",++tes);
	}
}