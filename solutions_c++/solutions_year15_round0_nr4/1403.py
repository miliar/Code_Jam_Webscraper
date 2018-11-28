#include <bits/stdc++.h>

using namespace std;

int t,x,r,c,m;
int ans;

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		scanf("%d%d%d",&x,&r,&c);
		m = min(r,c);
		if (x >= 7) ans = 0;
		else {
			if (((r*c) % x) != 0) ans = 0;
			else {
				if (x <= 2) ans = 1;
				else if (x == 3){
					if (m == 1) ans = 0;
					else ans = 1;
				} else if (x == 4){
					if (m <= 2) ans = 0;
					else {
						ans = 1;
					}
				} else if (x == 5){
					if (m <= 3) ans = 0;
					else {
						ans = 1;
					}
				} else if (x == 6){
					if (m <= 3) ans = 0;
					else {
						ans = 1;
					}
				}
			}
		}
		if (ans) printf("Case #%d: GABRIEL\n",jj);
		else printf("Case #%d: RICHARD\n",jj);
	}
	return 0;
}
