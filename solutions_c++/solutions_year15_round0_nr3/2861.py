#include <vector>
#include <queue>
#include <climits>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef long long LL;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef pair <int, int> PI;
typedef vector <PI> VPI;

int main()
{
	int T; cin >> T;
	FOR(kase, 1, T+1)
	{
		int L, K; cin >> L >> K;
		string s; cin >> s;
		string in;

		REP(i, K)
		in += s;

		vector <string> dp(in.sz);
		dp[0] = in[0];

		cout << "Case #" << kase << ": ";

		FOR(i, 1, in.sz)
		{
			if(dp[i-1] == "-1" && in[i] == 'i')
			dp[i] = "-i";
			if(dp[i-1] == "-1" && in[i] == 'j')
			dp[i] = "-j";
			if(dp[i-1] == "-1" && in[i] == 'k')
			dp[i] = "-k";
			if(dp[i-1] == "-i" && in[i] == 'i')
			dp[i] = "1";
			if(dp[i-1] == "-i" && in[i] == 'j')
			dp[i] = "-k";
			if(dp[i-1] == "-i" && in[i] == 'k')
			dp[i] = "j";
			if(dp[i-1] == "-j" && in[i] == 'i')
			dp[i] = "k";
			if(dp[i-1] == "-j" && in[i] == 'j')
			dp[i] = "1";
			if(dp[i-1] == "-j" && in[i] == 'k')
			dp[i] = "-i";
			if(dp[i-1] == "-k" && in[i] == 'i')
			dp[i] = "-j";
			if(dp[i-1] == "-k" && in[i] == 'j')
			dp[i] = "i";
			if(dp[i-1] == "-k" && in[i] == 'k')
			dp[i] = "1";
			if(dp[i-1] == "1" && in[i] == 'i')
			dp[i] = "i";
			if(dp[i-1] == "1" && in[i] == 'j')
			dp[i] = "j";
			if(dp[i-1] == "1" && in[i] == 'k')
			dp[i] = "k";
			if(dp[i-1] == "i" && in[i] == 'i')
			dp[i] = "-1";
			if(dp[i-1] == "i" && in[i] == 'j')
			dp[i] = "k";
			if(dp[i-1] == "i" && in[i] == 'k')
			dp[i] = "-j";
			if(dp[i-1] == "j" && in[i] == 'i')
			dp[i] = "-k";
			if(dp[i-1] == "j" && in[i] == 'j')
			dp[i] = "-1";
			if(dp[i-1] == "j" && in[i] == 'k')
			dp[i] = "i";
			if(dp[i-1] == "k" && in[i] == 'i')
			dp[i] = "j";
			if(dp[i-1] == "k" && in[i] == 'j')
			dp[i] = "-i";
			if(dp[i-1] == "k" && in[i] == 'k')
			dp[i] = "-1";
		}

		//REP(i, dp.sz)
		//cout << dp[i] << "\n";

		if(dp[in.sz - 1] != "-1")
		{
			cout << "NO\n";
			continue;
		}

		bool good = false;
		REP(i, in.sz)
		{
			if(dp[i] == "i")
			{
				FOR(j, i+1, in.sz-1)
				{
					if(dp[j] == "k")
					{
						good = true;
						break;
					}
				}
				if(good)
				break;
			}
		}

		dp[in.sz - 1] == "-1" && good ? cout << "YES\n" : cout << "NO\n";
	}

	return 0;
}
