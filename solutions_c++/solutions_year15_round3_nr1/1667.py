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
ll R,C,W;
#if 0
ll dp[(1<<10)+1];
ll aasolve(ll named)
{
	if(dp[named]!=-1)
		return dp[named];

	ll prev=-1;
	ll msk = named;
	bool ok=true;
	ll longest=0;
	for(int i=0;i<C;++i)
	{
		if(msk&1)
		{
			prev = i;
		}else{
			if(i-prev>=W){
				ok=false;
			}
			longest = max(longest, i-prev);
		}
		msk>>=1;
	}
	if(ok&&msk!=named)
	{
	//	cout<<longest<<";"<<named<<";"<<endl;
		dp[named]=longest;
		return longest;
	}

	
	ll result = 1e10;
	for(ll i=0;i<C-W+1;++i)
	{
		if((named>>i)&1)continue;
		ll val = solve(named|(1<<i) );
	//	cout<<i<<";"<<msk<<";"<<val<<endl;
		result=min(result, 1+val);
	}
	
	dp[named]=result;
	return result;
}

ll longest;
ll solve2(ll len)
{
	if(len<W)
	{
		return 0;
	}
	if(len==W)
	{
			longest=max(longest,len);

	}

	len -= 1;
	ll left = len/2;
	ll right = len - len/2;
	if(left<=W&&right<=W)
	{
		ll mini=min(left,right);
		ll maxi=max(left,right);
		
		if(mini==0)
		{
			return 0;
		}else{
			return 1;
		}
		
	}


	ll result = 0;
	result=solve2(left)+solve2(right)+1;
	return result;
}
#endif
int main()
{
    ios::sync_with_stdio(false);
	int T;
	cin>>T;
	for(int _t=0; _t<T; ++_t)
	{
		cerr<<"processing: " << _t+1<<endl;
		cin>>R>>C>>W;
		ll result = 0;
		if(C==W||W==1)
		{result=C;
		}else{
		
			int cnt=0;
			int pos=0;
			while(pos<C)
			{
				++cnt;
				pos+=W;
			}
			result=cnt+W-1;
		}
		cout<<"Case #"<<_t+1<<": "<<result<<endl;
	}
	return 0;
}




