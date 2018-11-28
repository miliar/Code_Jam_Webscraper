#pragma warning(disable:4786)

#include <vector>
#include <string>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
typedef pair<int,int> PII;
#define REP(i,n) for (int i = 0; i < (n); i++)
#define ALL(c) c.begin(),c.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz size()

ifstream ifs;
ofstream ofs;

typedef long long ll;

void testcase(int tst)
{
	int n, m;
	ifs >> n >> m;

	VVI a(n, VI(m, 0));
	REP(j, n)
		REP(i, m)
			ifs >> a[j][i];

	VI wj(n, 0);
	VI wi(m, 0);

	while (true) {
		int mn = 10000;
		REP(j, n)
			if (!wj[j])
				REP(i, m)
					if (!wi[i])
						mn = min(mn, a[j][i]);

		if (mn == 10000) {
			ofs << "Case #" << tst+1 << ": " << "YES" << endl;
			return;
		}

		bool found = false;
		REP(j, n) if (!wj[j]) {
			bool ok = true;
			REP(i, m) if (!wi[i] && a[j][i] != mn) ok = false;
			if (ok) {
				found = true;
				wj[j] = 1;
				break;
			}
		}

		if (found) continue;

		REP(i, m) if (!wi[i]) {
			bool ok = true;
			REP(j, n) if (!wj[j] && a[j][i] != mn) ok = false;
			if (ok) {
				found = true;
				wi[i] = 1;
				break;
			}
		}

		if (!found) {
			ofs << "Case #" << tst+1 << ": " << "NO" << endl;
			return;
		}
	}

}

int main()
{
	ifs.open("input.txt");
	ofs.open("output.txt");
	
	int t;
	ifs >> t;
	REP(tn, t)
	{
		testcase(tn);
	}

	return 0;
} 
