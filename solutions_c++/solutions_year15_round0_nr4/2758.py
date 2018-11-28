#include <stdio.h>
void win() { printf("RICHARD\n"); }
void lose() { printf("GABRIEL\n"); }
int main() {
	int t;
	scanf("%d", &t);
for(int tCount = 1; tCount <= t; tCount++) {
	int x, r, c;
	scanf("%d %d %d", &x, &r, &c);
	printf("Case #%d: ", tCount);
	if(x == 1) lose();
	else if((r*c == x && x != 2) || (r*c)%x != 0 || (r < x && c < x)) win();
	else if(x == 2) {
		if((r*c)%2 == 0) lose();
		else win();
	}
	else if(x == 3) {
		if(r > 1 && c > 1) lose();
		else win();
	}
	else if(x == 4) {
		if(r > 1 && c > 1) {
			if(r == 2 || c == 2) win();
			else lose();
		}
		else win();
	}
}
	return 0;
}