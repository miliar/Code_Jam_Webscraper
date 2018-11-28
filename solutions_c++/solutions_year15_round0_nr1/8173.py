#include <cstdio>

int main(int argc, char **argv)
{
	freopen("A-large.in","r",stdin);
	freopen("output","w",stdout);
	int t, max, curr = 0, need = 0;
	char sj;
	scanf("%i", &t);
	for (int i = 1; i <= t; ++i){
		scanf("%d", &max);
		scanf("%c", &sj);
		scanf("%c", &sj);
		curr += sj - '0';
		for(int j = 1; j <= max; ++j){
			scanf("%c", &sj);
			sj -= '0';
			if (sj != 0){
				if (j > curr) {
					need += j - curr;
					curr += j - curr;
				}
				curr += sj;
			}
		}
		printf("Case #%d: %d\n", i, need);
		need = 0, curr = 0;
	}
	return 0;
}

