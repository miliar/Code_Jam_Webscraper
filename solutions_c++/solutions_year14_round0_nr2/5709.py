# include <iostream>
# include <cstdio>

using namespace std;

double ccc, fff, x, ans;

double nope, heiti, timerywe, k;

void solve ()
{
        int i;
        nope = 0.0;
		timerywe = 0.0;
		heiti = 2.0;
		for (i = 0; i < 1;)
		{
			///cccout << ccc << " " << heiti << " " << x << " " << nope << " " << time << endl;
			k = (ccc - nope) / heiti;
			if ((x - nope) / heiti + timerywe > (x / (heiti + fff)) + k + timerywe)
			{
				nope = 0.0;
				heiti += fff;
				timerywe += k;
				continue;
			}
				timerywe += (x - nope) / heiti;
				break;

		}
}


int main ()
{
	int i, da, tst;
	cin >> tst;
	for (da = 1; da <= tst; da ++)
	{
        cin >> ccc;
        cin >> fff;
        scanf ("%lf", &x);
        solve ();
		printf ("Case #%d: %.6lf\n", da, timerywe);
	}
	return 0;
}
