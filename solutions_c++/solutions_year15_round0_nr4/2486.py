#include <stdio.h>
FILE *in, *out;
#pragma warning(disable:4996)

int main(){
	out = fopen("4.out", "w");
	int t, x, r, c;
	bool rick;
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		scanf("%d %d %d", &x, &r, &c);
		if (x == 1){
			rick = false;
		}
		if (x == 2){
			if (r*c % 2 == 1){
				rick = true;
			}
			else{
				rick = false;
			}
		}
		if (x == 3){
			if (r*c%3==0 && r*c>=6){
				rick = false;
			}
			else{
				rick = true;
			}
		}
		if (x == 4){
			if (r*c % 4 == 0 && r*c >= 12){
				rick = false;
			}
			else{
				rick = true;
			}
		}
		if (rick){
			fprintf(out,"Case #%d: RICHARD\n", i+1);
			printf("Case #%d: RICHARD\n", i + 1);
		}
		else{
			fprintf(out,"Case #%d: GABRIEL\n", i+1);
			printf("Case #%d: GABRIEL\n", i + 1);
		}
	}
}


