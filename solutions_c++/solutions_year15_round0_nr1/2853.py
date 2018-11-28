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
#include <stdio.h>
#define sf scanf
#define pf printf
#define ll long long
#define ull unsigned long long

#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for(int i = a; i < b; ++i )

using namespace std;


int main()
{
	int T;
	cin>>T;
	fr(c,0,T)
	{
		int n;
		cin>>n;
		string str;
		cin>>str;
		int num = 0;
		int ans= 0;
		fr(i,0,n+1)
		{
			ans += max(0, i - num );
			num += max(0, i-num);
			num += str[i]-'0';	
			//cout<<num<<" "<<ans<<endl;
		}
		pf("Case #%d: %d\n",c+1, ans);
	}

}

