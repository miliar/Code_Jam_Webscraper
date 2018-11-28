#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <assert.h>
#include <memory.h>

#include <time.h>
#pragma comment(linker, "/STACK:100000000")
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(x) (int)(x).size()
#define ll long long
#define fr(i,a,b) for(int i = (a);i <= (b);i++)
#define fd(i,a,b) for(int i = (a);i >= (b);i--)

int ri(){int x;scanf("%d",&x);return x;}

int dp[1 << 12];

string s;
queue<int> st;

void go(int mask)
{
	for(int i = 0;i < s.length();i++)
	{
		int newMask = 0;
		for(int j = 0;j <= i;j++)
			if (!(mask & (1 << j)))
				newMask |= (1 << (i - j));
		for(int j = i + 1;j < s.length();j++)
			if (mask & (1 << j))
				newMask |= (1 << j);
		if (dp[newMask] == -1 || dp[newMask] > dp[mask] + 1)
		{
			dp[newMask] = dp[mask] + 1;
			st.push(newMask);
		}
	}

}

void solve()
{
	int test = ri();
	fr(testing,1,test)
	{
		memset(dp,-1,sizeof(dp));
		cin >> s;
		int mask = 0;
		for(int i = s.length() - 1;i >= 0;i--)
		{
			mask *= 2;
			if (s[i] == '-')
				mask++;
		}
		st.push(mask);
		dp[mask] = 0;
		while(!st.empty())
		{
			mask = st.front();
			st.pop();
			go(mask);
		}
		cout << "Case #" << testing << ": " << dp[0] << endl;
	}
}

int main()
{
    #ifndef ONLINE_JUDGE
			freopen("C:/Users/WhiteDevil/Desktop/input.txt","rt",stdin);
			freopen("C:/Users/WhiteDevil/Desktop/output.txt","wt",stdout);
	#else
		//freopen("input.in","rt",stdin);
		//freopen("output.out","wt",stdout);
	#endif
	
	solve();

    return 0;
}