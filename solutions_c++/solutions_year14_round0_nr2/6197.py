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

const double eps = 1e-6;

int main()
{
	int T;cin >> T;
	REP(kase,T)
	{
		// Begin code
		double C,F,X; cin >> C >> F >> X;
		double t1 = 0.0, t2 = 0.0;

		double start = 2.0, prevsum = 1000001.0;
		double ans = 100001.0;

		while(1)
		{
			t1 = X/start;
			if(t1 + t2 > prevsum)
			{
				ans = prevsum;
				break;
			}
			prevsum = t1 + t2;
			t2 = t2 + C/start;
			start += F;
		}

		cout << "Case #" << kase+1 << ": ";
		std::cout.precision(7);
		cout << std::fixed << ans << endl;
	}

	return 0;
}
