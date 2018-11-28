#include<iostream>
#include<iomanip>
#include<memory.h>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cs;
	double c, r, f, x;
	double timeused, exp,nexp;
	cin >> cs;
	for (int tc = 1; tc <= cs; tc++)
	{
		cin >> c >> f >> x;
		timeused = 0;
		r = 2;
		exp = x / r;
		while (1)
		{
			timeused += c / r;
			r += f;
			nexp = timeused + x / r;
			if (nexp < exp)
				exp = nexp;
			else
				break;
		}
		cout << fixed << setprecision(7) << "Case #"<<tc<<": "<<exp << endl;
	}
	return 0;
}