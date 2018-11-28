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

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

int solve(string s){
	if (s.length() == 1){
		if (s[0] == '+')
			return 0;
		else
			return 1;
	}else{
		int cnt = 0;
		for (int i = 1; i < s.length(); ++i){
			if (s[i-1] == s[i]) continue;
			++cnt;
		} // end for
		if (s[s.length() -1] == '-') ++cnt;

		return cnt;
	}
	
	return -1;
}		

int main()
{
	ios_base::sync_with_stdio(0);
	int T; cin >> T;
	rep (i, T){
		string s; cin >> s;
		int ans = solve(s);
		cout << "Case #" << i+1 << ": " << ans << endl;
	} // end rep

	return 0;
}
