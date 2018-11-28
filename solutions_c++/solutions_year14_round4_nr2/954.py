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
	int n;
	ifs >> n;

	VI a(n, 0);
	REP(i, n)
		ifs >> a[i];

	int res = 0;

	int l = 0;
	int r = n-1;
	REP(i, n) {
		int min = 2000000000;
		int mj = 0;
		for (int j = l; j <= r; j++)
			if (min > a[j]) {
				min = a[j];
				mj = j;
			}

		if (mj - l < r - mj) {
			res += mj - l;
			for (int j = mj; j > l; j--)
				swap(a[j], a[j-1]);
			l++;
		} else {
			res += r - mj;
			for (int j = mj; j < r; j++)
				swap(a[j], a[j+1]);
			r--;
		}
	}

	ofs << "Case #" << tst+1 << ": " << res << endl;
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
