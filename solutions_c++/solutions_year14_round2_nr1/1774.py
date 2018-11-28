# include <iostream>
# include <fstream>
# include <algorithm>
# include <cmath>
# include <cstdio>
# include <cstdlib>
# include <cstring>
# include <string>
# include <vector>
# include <stack>
# include <queue>
# include <map>

using namespace std;

int n;

string a, b;

int main ()
{
	int t, te, sza, szb, l, r, ans, lamp;
	cin >> t;
	for (te = 1; te <= t; te ++)
	{
		cin >> n;
		cin >> a;
		cin >> b;
		sza = a.size ();
		szb = b.size ();
		l = 1;
		r = 1;
		ans = lamp = 0;
		if (a[0] != b[0]) lamp = 1;
		while (!lamp)
		{
			if (l == sza && r == szb) break;
			if (l < sza && r < szb && a[l] == b[r])
			{
				l ++;
				r ++;
				continue ;
			}
			if (l < sza && a[l] == b[r - 1])
			{
				l ++;
				ans ++;
				continue ;
			}
			if (r < szb && a[l - 1] == b[r])
			{
				r ++;
				ans ++;
				continue;
			}
			lamp = 1;
		}
		cout << "Case #" << te << ": ";
		if (lamp == 0) 
			cout << ans << endl;
		else 
			cout << "Fegla Won" << endl; 
	}


	return 0;
}

