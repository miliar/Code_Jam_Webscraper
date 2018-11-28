#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>	// require sort next_permutation count __gcd reverse etc.
#include <cstdlib>	// require abs exit atof atoi 
#include <cstdio>		// require scanf printf
#include <functional>
#include <numeric>	// require accumulate
#include <cmath>		// require fabs
#include <climits>
#include <limits>
#include <cfloat>
#include <iomanip>	// require setw
#include <sstream>	// require stringstream 
#include <cstring>	// require memset
#include <cctype>		// require tolower, toupper
#include <fstream>	// require freopen
#include <ctime>		// require srand
#define rep(i,n) for(int i=0;i<(n);i++)
#define ALL(A) A.begin(), A.end()
#define each(i,c) for(auto i=(c).begin();i!=(c).end();++i)
#define exist(s,e) ((s).find(e)!=(s).end())
#define clr(a) memset((a),0,sizeof(a))
#define nclr(a) memset((a),-1,sizoef(a))
#define sz(s) (int)((s).size())
#define INRANGE(x,s,e) ((s)<=(x) && (x)<(e))
#define pb push_back
#define MP(x,y) make_pair((x),(y))
#define INF 99999999999999999LL
using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef pair<string,string> SS;

set<string> C, J;

void dfs (string curr, bool sw){
	bool ok = true;
	rep (i, curr.length()){
		if (curr[i] == '?'){
			ok = false;
		} // end if
	} // end rep
	if (ok){
		if(sw){
			J.insert(curr);
		}else{
			C.insert(curr);
		} // end if
//		cerr << curr << endl;
		return;	
	} // end if
	rep (i, curr.length()){
		if (curr[i] == '?'){
			rep (j, 10){
				curr[i] = (char)('0'+j);
				dfs(curr, sw);
			} // end rep
		} // end if
	} // end rep
}

ll stoll(string s){
	stringstream ss(s);
	ll res;
	ss >> res;
	return res;
}

ll calc_diff(string c, string j){
	return (stoll(c) - stoll(j));
}

SS solve(string c, string j){
	C.clear(), J.clear();
	dfs(c, false);
	dfs(j, true);
	SS res = SS("","");
	ll diff = INF;	
	set<string>::iterator it = C.begin();
	for(; it != C.end(); ++it){
		string c = (*it);
		set<string>::iterator jt = J.begin();
		for (; jt != J.end(); ++jt){
			string j = (*jt);
			ll curr = abs(calc_diff(c,j));
//				cerr << "curr: " << curr << endl;
			if (curr < diff){
//				cerr << "c: " << c << " j: " << j << endl;
				diff = curr;
				res = SS(c, j);
			} // end if
		} // end for
	} // end for

	return res;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int T; cin >> T;
	rep (i, T){
		string c, j; cin >> c >> j;
		SS res = solve(c,j);
		cout << "Case #" << i+1 << ": " << res.first << ' ' << res.second << endl;
	} // end rep

	return 0;
}
