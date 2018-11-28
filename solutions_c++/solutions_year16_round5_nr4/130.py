#include <bits/stdc++.h>

using namespace std;

int t,tes,i,j,k,l,n;
bool ada0,valid;
char dum[107],s[107][107];

int main() {
	scanf("%d",&t);
	for (tes=1; tes<=t ; tes++) {
		scanf("%d%d",&n,&l);
		for (i=0 ; i<n ; i++) scanf("%s",s[i]);
		scanf("%s",&dum);
		
		valid = true;
		for (i=0 ; i<n ; i++) {
			ada0 = false;
			//printf("%s\n",s[i]);
			for (j=0 ; j<l ; j++) if (s[i][j] == '0') ada0 = true;
			if (!ada0) valid = false;
		}
		printf("Case #%d: ",tes);
		if (!valid) printf("IMPOSSIBLE\n"); else {
			printf("0");
			for (i=0 ; i<l-1 ; i++) printf("1");
			printf(" 0");
			for (i=0 ; i<l ; i++) printf("0?");
			printf("\n");
		}
	}
}
