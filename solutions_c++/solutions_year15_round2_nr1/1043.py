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
ll used[1000001];


ll rev(ll n)
{
	vector<ll> in;
//	cout<<"--"<<n<<"--"<<endl;
	while(n)
	{
		in.push_back(n%10);
		n/=10;
	}
	ll result =0;
	for(int i=0;i<in.size();++i)
	{
		result = result*10 + in[i];
	}
//	cout<<"--"<<result<<"--,"<<endl;
	return result;
}
int main()
{
    ios::sync_with_stdio(false);
	int T;
	cin>>T;
	for(int _t=0; _t<T; ++_t)
	{
		cerr<<"processing: " << _t+1<<endl;

		ll N;
		cin>>N;

		memset(used,0,sizeof(used));

		queue<ll> q, cnt;
		q.push(1);
		used[1]=1;
		cnt.push(1);

		while(!used[N])
		{
			ll val = q.front();
			q.pop();
			
			ll count = cnt.front();
			cnt.pop();

			if(used[val+1]==0 || used[val+1]>count+1)
			{
				q.push(val+1);
				cnt.push(count+1);
				used[val+1] = count+1;
			}
			
			ll revVal = rev(val);

			if(used[revVal]==0|| used[revVal]>count+1)
			{
				q.push(revVal);
				cnt.push(count+1);
				used[revVal] = count+1;
			}
		}

	
		cout<<"Case #"<<_t+1<<": "<<used[N]<<endl;
	}
	return 0;
}
