#include <cstdio>

int find(int set) {
	for (int i = 1; i <= 16; i++)
		if (set & (1 << i))
			return i;
	}

int main(void) {
	int T;
	int s[16];
	int Vrow, Mrow;
	int f_set, s_set, ans_set;

	scanf("%d", &T);

	for (int i = 1; i <= T; i++) {
		scanf("%d", &Vrow);

		for (int j = 0; j < 16; j++)
			scanf("%d", &s[j]);
		
		f_set = 0;
		for (int j = 0; j < 4; j++)
			f_set |= (1 << s[(Vrow -1)*4 + j]);

		scanf("%d", &Mrow);

		for (int j = 0; j < 16; j++)
			scanf("%d", &s[j]);
		
		s_set = 0;
		for (int j = 0; j < 4; j++)
			s_set |= (1 << s[(Mrow -1)*4 + j]);

		ans_set = f_set & s_set;

		printf("Case #%d: ", i);

		if (!ans_set)
			puts("Volunteer cheated!");
		else if (ans_set == (ans_set & (-ans_set)))
			printf("%d\n", find(ans_set));
		else 
			puts("Bad magician!");
		}

	return 0;
	}
