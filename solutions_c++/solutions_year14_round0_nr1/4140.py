#include <cstdio>

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 1; t <= T; t++) {
		int r, m1, m2;
		m1 = m2 = 0;
		scanf("%d" , &r);
		for(int i = 0; i < 4; i++) {
			if(i+1 == r)
				for(int j = 0; j < 4; j++) {
					int s;
					scanf("%d", &s);
					m1 |= 1 << s;
				}
			else
				for(int j = 0; j < 4; j++)
					scanf("%*d");
		}
		scanf("%d" , &r);
		for(int i = 0; i < 4; i++) {
			if(i+1 == r)
				for(int j = 0; j < 4; j++) {
					int s;
					scanf("%d", &s);
					m2 |= 1 << s;
				}
			else
				for(int j = 0; j < 4; j++)
					scanf("%*d");
		}

		printf("Case #%d: ", t);
		int m = m1 & m2;
		int pop = __builtin_popcount(m);
		if(pop == 0)
			printf("Volunteer cheated!\n");
		else if(pop > 1)
			printf("Bad magician!\n");
		else printf("%d\n", __builtin_ctz(m));
	}
	return 0;
}
