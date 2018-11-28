#include <stdio.h>

int N;
char input1[30], input2[30];
char ans1[30], ans2[30];
long long min_delta;
char a1[30], a2[30];

void search(int s);

void main()
{
	int i, j;

	scanf("%d", &N);

	for ( i = 1; i <= N; i++) {
		scanf("%s%s", &input1, &input2);

		min_delta = 9223372036854775800UL;
		for (j = 0; j < 20; j++) {
			ans1[j] = ans2[j] = 0;
		}
		search(0);

		printf("Case #%d: %s %s\n", i, a1, a2);
	}
}

void search(int s)
{
	if (input1[s] == '\0') {
		long long temp1 = 0, temp2 = 0;
		long long delta;

		for (int i = 0; i < ans1[i]; i++) {
			temp1 *= 10UL;
			temp1 += (ans1[i] - '0');
		}
		for (int i = 0; i < ans2[i]; i++) {
			temp2 *= 10UL;
			temp2 += (ans2[i] - '0');
		}
		if (temp1 >= temp2) {
			delta = temp1 - temp2;
		}
		else
			delta = temp2 - temp1;
		if (min_delta > delta) {
			int i;
			min_delta = delta;
			for ( i = 0; i < ans1[i]; i++)
				a1[i] = ans1[i];
			a1[i] = '\0';
			for ( i = 0; i < ans2[i]; i++)
				a2[i] = ans2[i];
			a2[i] = '\0';

		}
		return;
	}
	if (input1[s] == '?' && input2[s] == '?') {
		for (int i = 0; i < 10; i++) {
			ans1[s] = i + '0';
			for (int j = 0; j < 10; j++) {
				ans2[s] = j + '0';
				search(s + 1);
			}
		}
	}
	else if (input1[s] == '?') {
		ans2[s] = input2[s];

		for (int i = 0; i < 10; i++) {
			ans1[s] = i + '0';
			search(s + 1);
		}
	}
	else if (input2[s] == '?') {
		ans1[s] = input1[s];

		for (int i = 0; i < 10; i++) {
			ans2[s] = i + '0';
			search(s + 1);
		}
	}
	else {
		ans1[s] = input1[s];
		ans2[s] = input2[s];
		search(s + 1);
	}
}