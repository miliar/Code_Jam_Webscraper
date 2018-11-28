#include <cstdio>

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; i++) {
		bool b[17];
		for(int j = 1; j <= 16; j++)
			b[j] = false;
		int r;
		scanf("%d", &r);
		for(int j = 0; j < 16; j++) {
			int t;
			scanf("%d", &t);
			if(j/4 == r-1)
				b[t] = true;
		}
		int w = 0, l;
		scanf("%d", &r);
		for(int j = 0; j < 16; j++) {
			int t;
			scanf("%d", &t);
			if(j/4 == r-1 && b[t]) {
				w++;
				l = t;
			}
		}
		printf("Case #%d: ", i+1);
		if(w == 0)
			printf("Volunteer cheated!\n");
		if(w == 1)
			printf("%d\n", l);
		if(w > 1)
			printf("Bad magician!\n");
	}
	return 0;
}