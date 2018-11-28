#include <stdio.h>
#include <string.h>


char s[100010];
int t[100010];


int calc(int v, char ch)
{
	if (v < 0) return -calc(-v, ch);
	if (v == 1)
	{
		if (ch == 'i') return 2;
		if (ch == 'j') return 3;
		if (ch == 'k') return 4;
	}
	if (v == 2)
	{
		if (ch == 'i') return -1;
		if (ch == 'j') return 4;
		if (ch == 'k') return -3;
	}
	if (v == 3)
	{
		if (ch == 'i') return -4;
		if (ch == 'j') return -1;
		if (ch == 'k') return 2;
	}
	if (v==4)
	{
		if (ch == 'i') return 3;
		if (ch == 'j') return -2;
		if (ch == 'k') return -1;
	}
	return 0;
}


int gao()
{
	int l;
	long long xx;
	int x;
	int i, j;
	scanf ("%d%I64d", &l, &xx);
	if (xx >= 8)xx = 4 + xx%4;
	x = xx;
	memset (s, 0, sizeof(s));
	scanf ("%s", s);
	for (i = 0; i < l ;i++)
		for (j = 1; j < x; j++)
			s[i+j*l] = s[i];
	int last = 1;
	int state = 0;
	for (i = 0; i < x*l; i++)
	{
		t[i] = last = calc(last, s[i]);
		if (t[i] == 2 && state == 0)state++;
		if (t[i] == 4 && state == 1) state++;
	}
	if (last != -1)return 0;
	if (state != 2) return 0;
	return 1;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
	int T, i;
	scanf ("%d", &T);
	for (i = 1; i <= T; i++)
	{
		printf ("Case #%d: %s\n", i, gao()?"YES":"NO");
	}
	return 0;

}
