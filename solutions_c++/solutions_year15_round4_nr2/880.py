#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin("B-small-attempt1.in");
ofstream fout("output.txt");

int main()
{
	int tt, ti;
	fin >> tt;

	for(ti=1; ti<=tt; ti++)
	{
		fout << "Case #" << ti << ": ";
		////////////////////////////////////////////////////

		int n;
		long double v, x;

		fin >> n >> v >> x;

		if(n==1)
		{
			long double r, c;

			fin>>r>>c;

			if(c!=x)
				fout << "IMPOSSIBLE" << endl;
			else
			{
				fout.precision(30);
				fout << v/r << endl;
			}
		}
		if(n==2)
		{
			long double r[2], c[2];

			fin >> r[0] >> c[0]
				>> r[1] >> c[1];

			cout << "case" << ti << endl;
			cout << n << ' ' << v << ' ' << x << endl;
			cout << r[0] << ' ' << c[0] << endl;
			cout << r[1] << ' ' << c[1] << endl<<endl;

			if((c[0]<x && c[1]<x) || (c[0]>x && c[1]>x))
				fout << "IMPOSSIBLE" << endl;
			else if(c[0]==c[1])
			{
				fout << v/(r[0]+r[1]) << endl;
			}
			else
			{
				long double t0, t1;

				t1 = (v*x-v*c[0])/(r[1]*c[1]-r[1]*c[0]);
				t0 = (v-r[1]*t1)/r[0];

				fout.precision(30);
				if(t1>t0)
					fout << t1 << endl;
				else
					fout << t0 << endl;
			}
		}
	}

	return 0;
}