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

char dict[4][4][4] = { { {'G', 'G', 'G', 'G'}, {'G', 'G', 'G', 'G'}, {'G', 'G', 'G', 'G'}, {'G', 'G', 'G', 'G'} }, { {'R', 'G', 'R', 'G'}, {'G', 'G', 'G', 'G'}, {'R', 'G', 'R', 'G'}, {'G', 'G', 'G', 'G'} }, { {'R', 'R', 'R', 'R'}, {'R', 'R', 'G', 'R'}, {'R', 'G', 'G', 'G'}, {'R', 'R', 'G', 'R'} }, { {'R', 'R', 'R', 'R'}, {'R', 'R', 'R', 'R'}, {'R', 'R', 'R', 'G'}, {'R', 'R', 'G', 'G'}} };

int main()
{
	int T; cin >> T;
	FOR(kase, 1, T+1)
	{
		int X, R, C; cin >> X >> R >> C;
		cout << "Case #" << kase << ": ";

		dict[X-1][R-1][C-1] == 'R' ? cout << "RICHARD\n" : cout << "GABRIEL\n";
	}

	return 0;
}
