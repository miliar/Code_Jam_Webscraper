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

int count(int target, vector<ll> p)
{
	int result=0;
	for(int i=0;i<p.size();++i)
	{
		result +=  p[i]/(target);
		if(p[i]%target==0)--result;
	}
	result += target;

	return result;
}
int main()
{
	int T;
	cin>>T;
	for(int _t=0; _t<T; ++_t)
	{
		cerr<<"processing: " << _t+1<<endl;

		ll D;
		cin>>D;
		vector<ll> P(D);
		for(int i=0;i<D;++i)
		{
			cin>>P[i];
		}

		sort(P.begin(), P.end());

		int result = 1000;
		int l=0, r = 1001;
		for(int i=1000;i>=1;--i)
		{
			result = min(result, count(i,P));
		}

		cout<<"Case #"<<_t+1<<": "<<result<<endl;
	}
}
