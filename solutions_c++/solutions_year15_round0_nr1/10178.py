#include <cstdio>

int main() {
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
	{
		int sm, db = 0, cd= 0;
		scanf("%d", &sm);
		char s;
		scanf("%c", &s);
		for(int j = 0; j <= sm; ++j)
		{
			scanf("%c", &s);
			int c = s - '0';
			if(cd < j && c) {
				db += j - cd;
				cd = j;
			}
			cd += c;
		}
		printf("Case #%d: %d\n", i, db);
	}
	return 0;
}
