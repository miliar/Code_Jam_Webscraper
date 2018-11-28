#include <stdio.h>

int min(int x, int y) {
	return x<y ? x : y;
}

int max(int x, int y) {
	return x>y ? x : y;
}

int main() {
	int tc,x,r,c;
	scanf("%d",&tc);
	for(int t=1;t<=tc;t++) {
		scanf("%d %d %d",&x,&r,&c);
		if((x+1)/2 > min(r,c)) {
			printf("Case #%d: RICHARD\n",t);
			continue;
		}
		if(x > max(r,c)) {
			printf("Case #%d: RICHARD\n",t);
			continue;
		}
		if(((r*c)%x)!=0) {
			printf("Case #%d: RICHARD\n",t);
			continue;
		}
		if(x==4 && max(r,c)==4 && min(r,c)==2) {
			printf("Case #%d: RICHARD\n",t);
			continue;
		}

		printf("Case #%d: GABRIEL\n",t);
	}
}