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
	int n, x;
	ifs >> n >> x;

	VI a(n, 0);
	REP(i, n)
		ifs >> a[i];

	sort(ALL(a));

	reverse(ALL(a));
	VI was(n, 0);

	int cnt = 0;
	REP(i, n)
		if (!was[i]) {
			bool found = true;
			for (int j = i+1; j < n; j++)
				if (!was[j] && (a[i] + a[j] <= x)) {
					was[j] = 1;
					break;
				}
			cnt++;
		}

	ofs << "Case #" << tst+1 << ": " << cnt << endl;
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
