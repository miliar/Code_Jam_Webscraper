#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <iostream>
#include <climits>
#include <cstring>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

bool pal(tint n){
	stringstream strm; strm << n;
	string s; strm >> s;
	
	forn(i, s.size()) if(s[i] != s[s.size()-i-1])
		return false;
	return true;
}

int main()
{
#ifdef __YO__
	freopen("C-medium.in", "r", stdin);
	freopen("C-medium.out", "w", stdout);
#endif
	
	int T;
	cin >> T;
	
	vector<tint> vi;
	vi.push_back(0);
	for(tint i = 1; i < 10000009; ++ i){
		if(pal(i) && pal(i*i)){
			//cout << i*i << endl;
			vi.push_back(i*i);
		}
	}
	
	forn(t, T){
		tint a, b;
		cin >> a >> b;
		
		int ret = 0;
		forn(i, vi.size()) if(a <= vi[i] && vi[i] <= b)
			ret++;
		
		printf("Case #%i: %i\n", t+1, ret);
	}

	return 0;
}
