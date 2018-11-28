#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <numeric>
#include <tuple>
#include <climits>

#define INF 1023456789
#define SQR(x) ((x)*(x))
#define INIT(x,y) memset((x),(y),sizeof((x)))
#define SIZE(x) ((int)((x).size()))
#define REP(i, n) for (__typeof(n) i=0;i<(n);++i)
#define FOR(i, a, b) for (__typeof(a) i=(a);i<=(b);++i)
#define FORD(i, a, b) for (__typeof(a) i=(a);i>=(b);--i)
#define FORE(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

#define DEBUG
#ifdef DEBUG
#define DBG(x) cerr << #x << ": " << (x) << endl;
#else
#define DBG(x)
#endif

using namespace std;
 
typedef long long LL;
typedef pair<char,int> PI;
typedef tuple<int,int,int>trio;

inline void solve(int t)
{
	int N;
	cin >> N;
	string str;
	vector< vector<PI> >word(N);
	REP(i,N)
	{
		cin >> str;
		char c = '$';
		int cnt = 0;
		REP(j,str.size()) 
		{
			if (str[j]==c) cnt++;
			else
			{
				word[i].push_back(PI(c,cnt));
				int last = word[i].size() - 1;
				if (i!=0 && (word[i].size()>word[i-1].size() || word[i][last].first!=word[i-1][last].first))
				{
					cout << "Case #" << t << ": Fegla Won" << endl;
					return;
				}
				c = str[j];
				cnt = 1;
			}
		}
		word[i].push_back(PI(c,cnt));
		int last = word[i].size() - 1;
		if (i!=0 && (word[i].size()!=word[i-1].size() || word[i][last].first!=word[i-1][last].first))
		{
			cout << "Case #" << t << ": Fegla Won" << endl;
			return;
		}
	}
	int chars = word[0].size();
	vector<int>V(N);
	int ans = 0;
	REP(i,chars)
	{
		REP(j,N) 
		{
			V[j] = word[j][i].second;
			//cout << V[j] << endl;
		}
		//cout << "next" << endl;
		sort(V.begin(),V.end());
		int median = V[V.size()/2];
		int sum = 0;
		REP(j,N) sum += abs(V[j]-median);
		ans += sum;
	} 
	cout << "Case #" << t << ": " << ans << endl;
}

int main()
{
	int T;
	cin >> T;
	REP(i,T) solve(i+1);
        return 0;
}
