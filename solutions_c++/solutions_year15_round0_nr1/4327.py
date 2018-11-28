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
		int N; cin >> N;
		string s; cin >> s;

		int sum = 0, ans = 0;
		if(s[0] == '0')
		ans++, sum++;
		else sum += (s[0] - '0');

		FOR(i, 1, s.sz)
		{
			if(sum < i)
			{
				int diff = (i - sum);
				sum += diff;
				ans += diff;
			}
			sum += (s[i] - '0');
		}

		cout << "Case #" << kase << ": " << ans << "\n";
	}

	return 0;
}
