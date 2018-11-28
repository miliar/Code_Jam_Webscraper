#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FILE_NAME "C-small"

using namespace std;

bool poli(string& s)
{
	string s2(s.rbegin(), s.rend());
	return s == s2;
}

long long fs[21] = {  1,
					4,
					9,
					121,
					484,
					10201,
					12321,
					14641,
					40804,
					44944,
					1002001,
					1234321,
					4008004,
					100020001,
					102030201,
					104060401,
					121242121,
					123454321,
					125686521,
					400080004,
					404090404
};

bool poli(long long x)
{
	int n = 0;
	int d[128];
	while(x > 0)
	{
		d[n] = x % 10;
		x /= 10;
		++n;
	}
	for(int i = 0; i < n/2; ++i)
		if(d[i] != d[n-1-i])
			return false;
	return true;
}

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
	
	int numTestCaces = 0;
	cin >> numTestCaces;
	for(int Case = 1; Case <= numTestCaces; ++Case)
	{
		long long a, b;
		cin >> a >> b;
		long long cnt = 0;

//#define PRECALC
#ifdef PRECALC
		long long as = sqrt(a) - 2;
		if(as < 0) as = 0;
		long long bs = sqrt(b) + 2;
		for(int i = as; i <= bs; ++i)
		{
			if(poli(i) && poli(i*i) && a <= i*i && i*i <= b)
			{
				++cnt;
				cerr << i << ' ' << i*i << endl;
			}
		}
#else
		for(int i = 0; i < 21; ++i)
			if(a <= fs[i] && fs[i] <= b)
				++cnt;
#endif

		cout << "Case #" << Case << ": ";
		cout << cnt << endl;
	}

	return 0;
}
