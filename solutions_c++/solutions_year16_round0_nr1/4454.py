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

const int MAGIC = 73;

int go(int x)
{
	set <int> seen;
	FOR(i, 1, MAGIC)
	{
		int t = x*i;
		int n = t;
		while(n) {seen.insert(n%10); n/=10;}
		if(seen.sz == 10) return t;
	}

	return -1;
}

int main()
{
	int T;cin >> T;
	REP(c,T)
	{
		// Begin code
		int N; cin >> N;
		int ret = go(N);
		cout << "Case #" << c+1 << ": ";
		ret == -1 ? cout << "INSOMNIA\n" : cout << ret << "\n";
	}

	return 0;
}
