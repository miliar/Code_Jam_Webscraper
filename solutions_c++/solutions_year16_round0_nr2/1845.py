#include <cstdio>

int main()
{
	int T;	scanf("%d", &T);
	char in[105];
	for(int i = 0; i < T; ++i) {
		scanf("%s", in);
		int turn = 0, len = 0;
		for(len = 1; in[len] != '\0'; ++len)
			if(in[len] != in[len - 1])
				++turn;
		turn += (in[len - 1] == '-');
		printf("Case #%d: %d\n", i + 1, turn);
	}
	return 0;
}