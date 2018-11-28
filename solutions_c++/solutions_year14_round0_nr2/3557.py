#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>

#define Inf 2147483647
#define Pi acos(-1.0)
#define N 1000000
#define LL long long

inline LL Power(int b, int p) { LL ret = 1; for ( int i = 1; i <= p; i++ ) ret *= b; return ret; }
const int dr [] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dc [] = {0, 1, 1, 1, 0, -1, -1, -1};

#define F(i, a) for( int i = (0); i < (a); i++ )
#define Fs(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fe(i, x) for(typeof (x.begin()) i = x.begin(); i != x.end (); i++)
#define Set(a, s) memset(a, s, sizeof (a))
#define Max(a, b)  (a < b ? b : a)
#define Min(a, b)  (a > b ? b : a)

using namespace std;

int main(int argc, const char ** argv) 
{
	int t;
	cin>>t;
	for (int loop = 0; loop < t; ++loop)
	{
		std::vector<int> v;
		// if farm, farm early
		int i = 0;
		double best = std::numeric_limits<double>::max();
		double c, f, x;
		cin>>c>>f>>x;
		while(true)
		{
			double lt = 0.f, t2b, rate = 2.f;
			for (int ii = 0; ii < i; ++ii)
			{
				t2b = c/rate;
				lt += t2b;
				rate += f;
			}
			lt += x/rate;
			// printf("%d %.7f\n", i, lt);
			if (lt < best) best = lt;
			else break;
			i++;
		}
		printf("Case #%d: %.7f\n", loop+1, best);
	}
    return 0;	
}