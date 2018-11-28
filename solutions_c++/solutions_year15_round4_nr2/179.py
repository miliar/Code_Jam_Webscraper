#include<fstream>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<functional>
#include<numeric>
#include<bitset>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define mp make_pair

namespace
{
	int n;
	double V, X;
	double r[101], c[101];

	bool can(double t)
	{
		//double target = V * X;
		double target = 0.0;
		double vLo = 0.0, vxLo = 0.0, vHi = 0.0, vxHi = 0.0;
		for (int i = 0; i < n; ++i)
		{
			double maxV = r[i] * t;
			double neededV = V - vLo;
			double usedV = min(maxV, neededV);

			vLo += usedV;
			vxLo += usedV * c[i];
			if (usedV == neededV)
				break;
		}

		for (int i = n-1; i >= 0; --i)
		{
			double maxV = r[i] * t;
			double neededV = V - vHi;
			double usedV = min(maxV, neededV);

			vHi += usedV;
			vxHi += usedV * c[i];
			if (usedV == neededV)
				break;
		}

		//return ((vxLo - target) / target <= 1e-10 && (vxHi - target)/target >= -1e-10);
		return (vxLo <= target + 1e-20 && vxHi >= target - 1e-20);
	}
}

//int main15R2_B()
int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	//ifstream fin("test.in");
	//ofstream fout("test.out");

	fout << std::fixed << std::setprecision(9);

	unsigned int numberOfCases;
	fin >> numberOfCases;

	for (unsigned int zz = 1; zz <= numberOfCases; ++zz)
	{
		fin >> n >> V >> X;
		vector<pair<double, double> >vp(n);
		for (int i = 0; i < n; ++i)
		{
			fin >> vp[i].second >> vp[i].first;
		}

		sort(vp.begin(), vp.end());
		for (int i = 0; i < n; ++i)
		{
			r[i] = vp[i].second;
			ll cc = ll(10000 * vp[i].first + .5) - ll(10000 * X + .5);
			c[i] = 0.0001 * cc;
		}

		if (c[0] > 1e-10 || c[n - 1] < -1e-10)
		{
			fout << "Case #" << zz << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			double sumR = accumulate(r, r + n, 0.0);
			double tLo = V / sumR;
			double tHi = tLo * 2;

			while (!can(tHi))
			{
				tLo = tHi;
				tHi *= 2;
			}

			int its = 100000;
			while (its-- > 0)
			{
				double t = (tHi + tLo) * 0.5;
				if (can(t))
					tHi = t;
				else
					tLo = t;
			}

			fout << "Case #" << zz << ": " << ((tHi + tLo) * 0.5) << endl;
		}
	}

	return 0;
}
