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


// a>bが前提
ll gcd(ll a, ll b){
        return (b>0)? gcd(b, a%b) : a ;
}
ll lcm(ll a, ll b)
{
        if (a && b) return a / gcd(a, b) * b;
        return 0;
}


int main()
{
	int T;
	cin>>T;
	for(int _t=0; _t<T; ++_t)
	{
		cerr<<"processing: " << _t+1<<endl;

		ll B,N;
		cin>>B>>N;
		vector<ll> M(B);
		for(int i=0;i<B;++i)
			cin>>M[i];

		ll l = 1;
		for(int i=0;i<B;++i)
		{
			l = lcm(l, M[i]);
		}

		ll processed = 0;
		for(int i = 0; i < B; ++i)
		{
			processed += l/M[i];
		}
		//if(N>processed)
		cerr<<N<<";"<<processed<<endl;
		N %= processed;
		N += processed;

		ll result = B-1;
		vector<ll> Mt(B);


		for(int i=0;i<N;++i)
		{
			//sort(Mt.begin(), Mt.end());
			ll mini = *min_element(Mt.begin(), Mt.end());
			if(mini>0)
			{
				for(int j=0;j<B;++j)
				{
					Mt[j] -= mini;
				}
			}

			int index;
			for(int j=0;j<B;++j)
			{
				if(Mt[j]==0)
				{
					index = j;
					break;
				}
			}

			Mt[index] += M[index];

			if(i==N-1)
				result = index;
		}


		cout<<"Case #"<<_t+1<<": "<<result+1<<endl;
	}

	return 0;
}
