# include <cstdio>
# include <cmath>
# include <cstring>
# include <string>
# include <vector>
# include <queue>
# include <map>
# include <iostream>
# include <algorithm>

using namespace std;

int n, p, r, s;

vector <char> ans;

char a[16];

void check ()
{
	int i, j;
	vector <char> crr, nxt;
	for (i = 1; i <= (1 << n); i ++)
		crr.push_back (a[i]);
	if (crr > ans && ans[0] != 'I')
		return;
	for (i = n; i >= 1; i --)
	{
		nxt.clear ();
		for (j = 0; j < (1 << i); j += 2)
		{
			if (crr[j] == crr[j + 1])
				return;
			if (crr[j] == 'P' && crr[j + 1] == 'S')
				nxt.push_back ('S');
			if (crr[j + 1] == 'P' && crr[j] == 'S')
				nxt.push_back ('S');
				
			if (crr[j] == 'P' && crr[j + 1] == 'R')
				nxt.push_back ('P');
			if (crr[j + 1] == 'P' && crr[j] == 'R')
				nxt.push_back ('P');
				
			if (crr[j] == 'S' && crr[j + 1] == 'R')
				nxt.push_back ('R');
			if (crr[j + 1] == 'S' && crr[j] == 'R')
				nxt.push_back ('R');
		}
		
		crr.clear ();
		crr = nxt;
	}
	ans.clear ();
	for (i = 1; i <= (1 << n); i ++)
		ans.push_back (a[i]);
}

void go (int idx, int cp, int cr, int cs)
{
	///printf ("%d %d %d %d\n", idx, cp, cr, cs);
	if (idx > (1 << n))
	{
		check ();
		return;
	}
	if (cp)
		a[idx] = 'P', go (idx + 1, cp - 1, cr, cs);
	if (cr)
		a[idx] = 'R', go (idx + 1, cp, cr - 1, cs);
	if (cs)
		a[idx] = 'S', go (idx + 1, cp, cr, cs - 1);
}

int main ()
{
	int nt, t, i;
	scanf ("%d", &t);
	for (nt = 1; nt <= t; nt ++)
	{	
		ans.clear ();
		ans.push_back ('I');
		ans.push_back ('M');
		ans.push_back ('P');
		ans.push_back ('O');
		ans.push_back ('S');
		ans.push_back ('S');
		ans.push_back ('I');
		ans.push_back ('B');
		ans.push_back ('L');
		ans.push_back ('E');
		printf ("Case #%d: ", nt);
		scanf ("%d%d%d%d", &n, &r, &p, &s);
		go (1, p, r, s);
		for (i = 0; i < ans.size (); i ++)
			printf ("%c", ans[i]);
		printf ("\n");
	}
	return 0;
}

