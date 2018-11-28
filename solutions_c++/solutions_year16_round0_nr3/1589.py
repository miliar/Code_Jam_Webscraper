#include <cstdio>

int T, N, J;
int n, j;
int bin[250];
char JJ[][2] = {'0', '0', '1', '1'};
void fill_bin(int s)
{
	if(s == n) {
		for(int i = 0; i < n; ++i) {
			putchar(JJ[ bin[i] ][0]);
			putchar(JJ[ bin[i] ][1]);
		}
		puts("11 3 4 5 6 7 8 9 10 11");
		++j;
		if(j == J)	return;
		printf("11");
		return;
	}
	bin[s] = 0;
	fill_bin(s + 1);
	if(j == J)	return;
	
	bin[s] = 1;
	fill_bin(s + 1);
	if(j == J)	return;
	
	return;
}
int main()
{
	puts("case #1:");
	printf("11");
	
	scanf("%d%d%d", &T, &N, &J);
	n = N / 2 - 2;
	
	fill_bin(0);
	return 0;
}
