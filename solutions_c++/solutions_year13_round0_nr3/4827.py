#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int T, q = 1;

vector <int> pal;
vector <int> palsquare;

bool isPal (int x)
{
	char buf[1111 ]= "";
	itoa (x, buf, 10);
	int l = strlen (buf);
	for (int j=0; j<l/2; j++) {
		if (buf[j] != buf[l-1-j]) return 0;
	}
	return 1;
}

void make (void)
{
	for (int i=0; i<1000; i++) {
		if (isPal (i)) pal.push_back (i);
	}
	for (int i=0; i<pal.size(); i++) {
		if (isPal (pal[i]*pal[i])) palsquare.push_back (pal[i]*pal[i]);
	}
}

int main()
{
	make();
	for (scanf ("%d", &T); T--;)
	{
		int a, b;
		scanf ("%d%d", &a, &b);
		int st = lower_bound (palsquare.begin(), palsquare.end(), a) - palsquare.begin();
		int ed = upper_bound (palsquare.begin(), palsquare.end(), b) - palsquare.begin();
		int ans = ed - st;
		printf ("Case #%d: ", q++);
		printf ("%d\n", ans);
	}
	return 0;
}