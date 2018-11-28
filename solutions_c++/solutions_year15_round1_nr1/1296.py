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


int main()
{
    ios::sync_with_stdio(false);
	int T;
	cin>>T;
	for(int _t=0; _t<T; ++_t)
	{
		cerr<<"processing: " << _t+1<<endl;

		ll N,M;
		cin>>N;

		vector<ll> m(N);
		for(int i=0;i<N;++i)
		{
			cin>>m[i];
		}

		ll ans0=0;
		for(int i=1;i<N;++i)
		{
			ans0 += max(0ll, m[i-1]-m[i]);
		}

		ll ans1=1000000;
		ll l =0, r = 10000;
		for(int i=0;i<100;++i)
		{
			ll mid = (l+r)/2;

			bool ok = true;
			ll count = 0;
			for(int j=0;j<N-1;++j)
			{
				if(m[j]-mid>m[j+1])
				{
					ok = false;
				}
				count += min(m[j], mid);
			}

			if(ok)
			{
				ans1 = min(ans1, count);
				r= mid;
			}else{
				l = mid;
			}
		}
		
		cout<<"Case #"<<_t+1<<": "<<ans0<<" "<<ans1<<endl;
	}
}
