#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>

using namespace std;

typedef long long ll;
typedef long double ld;

//#define SMALL
#define LARGE
int main()
{
	freopen("B-test.in", "rt", stdin);
	freopen("B-test.out", "wt", stdout);
#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif

	int T;
	cin >> T;

	for(int ii=0; ii<T; ii++)
	{
		cout << "Case #" << (ii+1) << ": ";

		double C, F, X;
		cin >> C >> F >> X;

		double rate = 2.0;
		double purchaseTime = 0;
		double secondsToX = X / rate;

		bool done = false;
		while(!done)
		{
			purchaseTime += C / rate;
			rate += F;
			double newSecondsToX = X / rate;
			if(purchaseTime + newSecondsToX < secondsToX)
			{
				secondsToX = purchaseTime + newSecondsToX ;
			}
			else done = true;
		}

		cout.setf( std::ios::fixed, std:: ios::floatfield );
		cout.precision(7);
		cout << secondsToX << endl;


END_CASE:;
	}

	return 0;
}
