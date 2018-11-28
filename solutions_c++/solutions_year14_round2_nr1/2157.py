#include <cstdio>

using namespace std;

int T, x, N, ans;
char a [300];
char b [300];
char ta[300];
char tb[300];
int ah, bh, la, lb, tax, tbx, az, bz;
int ax[300];
int bx[300];

void init ()
{
	ans = 0;
	ah = bh = 0;
	for (int i=0; i < 120; ++i)
	{
		a[i] = b[i] = '\0';
		ax [i] = bx [i] = 0;
	}
}

int mabs (int x)
{
	return (x > 0) ? x : -x;
}

void mta ()
{
	az = 0;
	bool p = false;
	tax = 1;
	ta[0] = a[0];
	for (int i = 1; i < la; ++i)
		if (a[i] != a[i-1])
			ta[tax ++] = a[i];
	for (int i = 0; i < la; ++i)
		if (ta[az] == a[i])
			ax[az] ++;
		else
			az ++;
}

void mtb ()
{
	bz = 0;
	bool p = false;
	tbx = 1;
	tb[0] = b[0];
	for (int i = 1; i < lb; ++i)
		if (b[i] != b[i-1])
			tb[tbx ++] = b[i];
	for (int i = 0; i < lb; ++i)
		if (tb[bz] == b[i])
			bx[bz] ++;
		else
			bz ++;
}

bool equ ()
{
	if (tbx != tax)
		return false;
	for (int i=0; i < tax; ++i)
		if (ta[i] != tb[i])
			return false;
	return true;
}

/*void solve ()
{
	int i, j;
	for (i=0, j=0; i < la && j < lb; ++i, ++j)
	{

	}
}*/

void solve ()
{
	for (int i=0; i <= az; ++i)
		ans += mabs (ax[i] - bx[i]);
}

int main()
{
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
	scanf ("%d", &T);
	for (x = 1; x <= T; ++x)
	{
		init ();
		scanf ("%d\n", &N);
		scanf ("%s\n", a);
		scanf ("%s", b);
		for (la = 0; a[la] != '\0'; la ++)
			ah = ah | (1 << (a[la] - 'a'));
		for (lb = 0; b[lb] != '\0'; lb ++)
			bh = bh | (1 << (b[lb] - 'a'));
		mta (); 
		mtb ();
		printf ("Case #%d: ", x);
		if (ah != bh || !equ())
			printf ("Fegla Won\n");
		else
		{
			solve ();
			printf ("%d\n", ans);
		}
		//	printf ("%d\n", mabs (la - lb));
	}
	return 0;
}