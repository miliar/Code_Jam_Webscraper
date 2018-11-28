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
vector<int> alpha[26];

const string digit[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
map<char,int> d[10];
string ans;

void init_val(void){
	rep (i, 10) d[i].clear();
	rep (i, 10){
		rep (j, digit[i].length()){
			d[i][digit[i][j]]++;
		} // end rep
	} // end rep
}

bool is_empty(map<char,int> curr){
	rep (i, 26){
		if (curr[char('A'+i)] != 0) return false;
	} // end rep
	return true;
} 

void dfs(map<char,int> curr, int ind, string res){
	if (is_empty(curr)){
		ans = res;
		return;
	} // end if

	rep (i, 10){
		map<char,int> c = curr;
		bool ok = true;
		rep (j, 26){
			if (c[char('A'+j)] >= d[i][char('A'+j)]){
				c[char('A'+j)] -= d[i][char('A'+j)];
			}else{ 
				ok = false;
				break;
			} // end if
		} // end rep
		if (ok){
			dfs(c, ind + 1, (char)('0' + i) + res);
		} // end if
	} // end rep
} 

string solve(string s){
	
	ans = "";
	map<char,int> c; c.clear();
	rep (j, s.length()) c[s[j]]++;
	dfs(c, 0, "");

	return ans;	
}

int main()
{
	init_val();
	ios_base::sync_with_stdio(0);
	int T; cin >> T;
	rep (i, T){
		string s; cin >> s;
		string res = solve(s);
		cout << "Case #" << i+1 << ": " << res << endl;
	} // end rep

	return 0;
}
