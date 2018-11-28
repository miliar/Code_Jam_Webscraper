#include <cstring>
#include <string.h>
#include <map>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <list>

using namespace std;


int pal(double _a)
{
	ostringstream strs;
	strs.precision(100);
	strs << _a;
	string str = strs.str();

	string reversed = string ( str.rbegin(), str.rend() );

	if( str.compare(reversed) == 0 )
	{
		//cout << "String : " << str << " Reversed : " << reversed << "\n";
		return 1;
	}
	return 0;
}

#define SMALL
//#define LARGE
int main() {
	freopen("c.txt", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif

	int T, i;

	cin >> T;
	for( i=1; i<T+1; i++)
	{
		int res = 0;
		double ustart,uend, start, end, cur;
		cin >> ustart >> uend;
		start = ceil(sqrt(ustart));
		end = floor(sqrt(uend));

		for( cur=start ; cur <= end ; cur++)
		{
			if( pal(cur) )
			{
				double a = pow(cur, 2);
				if( pal(a) ) res++;
			}
		}
		cout << "Case #" << i << ": " << res << "\n";
	}
	return 0;
}
