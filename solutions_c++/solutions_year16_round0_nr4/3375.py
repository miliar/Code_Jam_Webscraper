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
	int T;cin >> T;
	REP(c,T)
	{
		// Begin code
		LL K, C, S; cin >> K >> C >> S;
		if(K == 1)
		{
			cout << "Case #" << c+1 << ": ";
			cout << K << "\n";
			continue;
		}

		// Handle first level Complexity
		if(C == 1)
		{
			cout << "Case #" << c+1 << ": ";
			REP(i, K-1) cout << i+1 << " ";
			cout << K << "\n";
			continue;
		}

		LL leafGroupSize = 1;
		REP(i, C-1) leafGroupSize *= K;
			
		if(C == 2)
		{
			cout << "Case #" << c+1 << ": ";
			REP(i, K-1)
			cout << i*K + (i+2) << " ";
			cout << "\n";
		}
		else
		{
			cout << "Case #" << c+1 << ": ";
			FOR(i, 1, K)
			{
				LL skip = (i-1) * (leafGroupSize);
				LL hop = skip + (i * ( leafGroupSize / K ));
				LL idx = hop + (i+1);
				cout << idx << " ";
			}
			cout << "\n";
		}
	}

	return 0;
}
