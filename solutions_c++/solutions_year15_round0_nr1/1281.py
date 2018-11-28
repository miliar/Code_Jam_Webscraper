#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <bitset>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <list>
#include <climits>
#include <assert.h>

//#include <gmpxx.h>

#ifdef _WIN32
#include <time.h>
#else
#include <sys/time.h>
#endif

using namespace std;
#define ll long long


bool ok(ll n, ll smax, string s)
{
	ll count = n;

	count += s[0] - '0';

	for(int i=1;i<s.length();++i)
	{
		if(i<=count)
		{
			count += s[i]-'0';
		}else{
			return false;
		}
	}
	return true;
}

int main()
{
	int T;
	cin>>T;
	for(int _t=0; _t<T; ++_t)
	{
		cerr<<"processing: " << _t+1<<endl;

		ll smax;
		string s;
		cin>>smax;
		cin>>s;

		ll result = 1e9;
		ll l=0, r=100000;
		for(int i=0;i<1000;++i)
		{
			ll m = (l+r)/2;

			if(ok(m, smax, s))
			{
				result = min(result, m);
				r = m-1;
			}else{
				l = m+1;
			}
		}
		
		cout<<"Case #"<<_t+1<<": "<<result<<endl;
	}
}
