#include <stdio.h>
#include <algorithm>

using namespace std;

int main() {
	freopen("om.in","r",stdin);
	freopen("om.out","w",stdout);
	int x,r,c,t;
	scanf("%d\n",&t);
	for (int tt=1;tt<=t;tt++) {
		scanf("%d %d %d\n",&x,&r,&c);
		printf("Case #%d: ",tt);
		if (x==1) {
			puts("GABRIEL");
		} else if (x==2) {
			if ((r*c)%2==0) {
				puts("GABRIEL");
			} else {
				puts("RICHARD");
			}
		} else if (x==3) {
			if ((r*c)%3!=0) {
				puts("RICHARD");
			} else {
				if (r==1||c==1) {
					puts("RICHARD");
				} else {
					puts("GABRIEL");
				}
			}
		} else {
			if ((r*c)%4!=0) {
				puts("RICHARD");
			} else {
				if (r*c==4||r*c==8) {
					puts("RICHARD");
				} else {
					puts("GABRIEL");
				}
			}
		}
	}
}