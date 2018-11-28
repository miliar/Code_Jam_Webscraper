#include <iostream>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <queue>

#include <math.h>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <string.h>
#include <string>
#include <stdio.h>
#define sf scanf
#define pf printf
#define ll long long

#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i = a; i < b; ++i )
#define pb push_back 

using namespace std;


#define Max 10000000  

string str;

string solve()
{
	string ans;

	for( int i = 0; i < str.size(); ++i )
	{
		if( ans.empty() )
		{
			ans = str[i];
		}
		else
		{
			string t1 = ans + str[i];
			string t2 = ""; t2 +=str[i]; t2 += ans;
			if( t1 > t2 )
			{
				ans = t1;
			}
			else
			{
				ans = t2;
			}
		}
	}
	return ans;
}

int main()
{
	int T;
	cin>>T;
	fr(c,0,T)
	{
		cin>>str;
		printf("Case #%d: %s\n",c+1,solve().c_str());
	}
}
