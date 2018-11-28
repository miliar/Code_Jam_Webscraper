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


ll bitCount(ll n)
{
	ll result=0;
	while(n)
	{
		if(n%2)++result;
		n>>=1;
	}
	return result;
}

int dr[4]={-1,0,1,0};
int dc[4]={0,1,0,-1};

int main()
{
	int T;
	cin>>T;
	for(int _t=0; _t<T; ++_t)
	{
		cerr<<"processing: " << _t+1<<endl;

		ll R,C, N, total;
		cin>>R>>C>>N;
		total = R*C;

		bool table[17][17];
		ll result = 1000000;

		for(ll msk=0;msk<(1<<total);++msk)
		{
			if(bitCount(msk)!=N)continue;

			memset(table,0,sizeof(table));

			ll alloc = msk;
			for(int i=0;i<total;++i)
			{
				if( (alloc>>i)&1)
				{
					table[i/C][i%C] = true;
				}
			}

			ll count = 0;
			for(int i=0;i<R;++i)
			{
				for(int c=1;c<C;++c)
				{
					if(table[i][c]&&table[i][c-1])
						++count;
				}
			}

			for(int i=0;i<C;++i)
			{
				for(int r=1;r<R;++r)
				{
					if(table[r-1][i]&&table[r][i])
						++count;
				}
			}

			result = min(result,count);
		}

		cout<<"Case #"<<_t+1<<": "<<result<<endl;
	}

	return 0;
}
