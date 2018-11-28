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
#include    <iomanip>

//#include <gmpxx.h>

#ifdef _WIN32
#include <time.h>
#else
#include <sys/time.h>
#endif

using namespace std;
#define ll long long


		vector<char> keys;
		
		string keystr,target;
		
		ll K,L,S;
ll genCount, result;
ll maxBanana;
void gen(string s)
{
	if(s.length()==S)
	{
		ll cnt =0;
		for(int i=0;i<=S-L;++i)
		{
			bool ok=true;
			for(int j=0;j<target.length();++j)
			{
				if(target[j]!=s[i+j])
				{
					ok=false;
					break;
				}
			}
			if(ok)++cnt;
		}
		maxBanana=max(maxBanana,cnt);
		result+=cnt;
		++genCount;
		return ;
	}

	for(int i=0;i<keys.size();++i)
	{
		s.push_back(keys[i]);
		gen(s);
		s.pop_back();
	}
}
int main()
{
	int T;
	cin>>T;
	for(int _t=0; _t<T; ++_t)
	{
		cerr<<"processing: " << _t+1<<endl;
		cin>>K>>L>>S;
		cin>>keystr;
		cin>>target;

		keys.clear();
		for(int i=0;i<keystr.length();++i)
		{
			keys.push_back(keystr[i]);
		}
		sort(keys.begin(),keys.end());
	//	unique(keys.begin(),keys.end());

		genCount =0;
		result = 0;
		maxBanana=0;
		gen("");
		//cout<<genCount<<";"<<result<<endl;
		cout<<"Case #"<<_t+1<<": ";
		cout<<setprecision(9)<<maxBanana-result/(double)genCount<<endl;
	}

	return 0;
}
