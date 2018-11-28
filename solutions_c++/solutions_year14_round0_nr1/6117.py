#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int i,j,k,l,n,t,m[6][6],cntans,ans;
bool possible[20];

int main() {
	scanf("%d", &t);
	for(l=1 ; l<=t ; l++) {
		scanf("%d", &n);
		for(i=1 ; i<= 4 ; i++) {
			for(j=1 ; j<=4 ; j++) {
				scanf("%d", &m[i][j]);
			}
		}
		
		memset(possible, false, sizeof(possible));
		cntans = 0;
		
		for(i=1 ; i<=4 ; i++) {
			possible[m[n][i]] = true;
		}
		
		scanf("%d", &n);
		for(i=1 ; i<= 4 ; i++) {
			for(j=1 ; j<=4 ; j++) {
				scanf("%d", &m[i][j]);
			}
		}
		
		for(i=1 ; i<=4 ; i++) {
			if(possible[m[n][i]]) {
				ans = m[n][i];
				cntans++;
			}
		}
		
		printf("Case #%d: ", l);
		if(cntans == 0) {
			printf("Volunteer cheated!\n");
		} else if(cntans > 1) {
			printf("Bad magician!\n");
		} else {
			printf("%d\n", ans);
		}
	}
	
	return 0;
}
