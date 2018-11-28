#pragma warning(disable:4996)
#include<stdio.h>
#define MAX 10006

int l, x, chk, testcase;
int t[MAX], sign[MAX];
char data[MAX];

int sign2[4][4] = {
	1, 1, 1, 1,
	1, -1, 1, -1,
	1, -1, -1, 1,
	1, 1, -1, -1
};
char gop[4][4] = {
	'1', '2', '3', '4',
	'2', '1', '4', '3',
	'3', '4', '1', '2',
	'4', '3', '2', '1' };

void process()
{
	for (int i = 1; i < x; i++)
	{
		for (int j = i * l + 1; j <= i * l + l; j++) data[j] = data[j - i *l];
	}
	for (int i = 1; i <= l * x; i++)
	{
		if (data[i] == 'i') data[i] = '2';
		if (data[i] == 'j') data[i] = '3';
		if (data[i] == 'k') data[i] = '4';
	}

	chk = 0;
	t[0] = '1';
	sign[0] = 1;
	for (int i = 1; i <= l * x; i++)
	{
		t[i] = gop[t[i - 1] - '1'][data[i] - '1'];
		sign[i] = sign[i - 1] * sign2[t[i - 1] - '1'][data[i] - '1'];

		if (chk == 0 && t[i] == '2' && sign[i] == 1) chk = 1;
		if (chk == 1 && t[i] == '4' && sign[i] == 1) chk = 2;
	}

	if (chk == 2 && t[l*x] == '1' && sign[l*x] == -1) chk = 3;
}

void input()
{
	scanf("%d", &testcase);
	for (int i = 1; i <= testcase; i++)
	{
		scanf("%d %d\n", &l, &x);
		gets(data + 1);
		process();

		if (chk == 3) printf("Case #%d: YES\n", i);
		else printf("Case #%d: NO\n", i);

		for (int j = 1; j <= l * x; j++) t[j] = sign[j] = data[j] = 0;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	input();
	return 0;
}