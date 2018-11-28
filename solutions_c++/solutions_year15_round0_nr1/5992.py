#include <stdio.h>

FILE *out = fopen("output.txt", "w");
int t;
int total;
int help;
int n;
int s[10001] = { NULL };

void input();
void process();

int main(void)
{
	input();
	return 0;
}

void input()
{
	int k;
	int i;
	char temp[10001];
	scanf("%d", &t);
	for (k = 1; k <= t; k++) {
		total = 0;
		help = 0;
		for (i = 0; i <= 10000; i++) {
			s[i] = 0;
			temp[i] = 0;
		}
		scanf("%d%s", &n,temp);
		for (i = 0; i <= n; i++)
			s[i] = temp[i] - '0';
		process();
		fprintf(out,"Case #%d: %d\n", k, help);
	}
}

void process()
{
	int i;
	total = s[0];
	for (i = 1; i <= n; i++)
	{
		if (total >= i) {
			total = total + s[i];
		} else {
			if (s[i] != 0) {
				help = help + (i - total);
				total = total + s[i] + (i - total);
			}
		}
	}
}