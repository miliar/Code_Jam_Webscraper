#include <queue>
#include <iostream>       
#include <string>
#include <vector>
#include <fstream>        
#include <functional> 
#include <algorithm>  
#include <cstdlib>    
#include <cstring>    
#include <map>        
#include <iomanip>    
#include <limits> 
#include <unordered_map>
#include <set>
#include <cmath>
#include <numeric> //accumulate
#include <stack>

//#include <unordered_set>//unordered_set

#define rep(i,a) for (int i = 0; i < (a); ++i)
#define rep2(i,a,b) for (int i = (a); i < (b); ++i)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define PI 3.14159265359;

using namespace std;
typedef long long ll;
typedef double lf;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<pair<int, int> > vpii;
typedef vector<vector<int> > vvi;
typedef const vector<int> cvi;
typedef vector<bool> vb;

int pre[26];
int nex[26];
bool vstd[26];
vector<int> sol;
void dfs(int here) {
	vstd[here] = true;
	if (nex[here] != -1)
		if (vstd[nex[here]] == false)
			dfs(nex[here]);
	sol.push_back(here);
}
int main() {
	FILE *fp;
	freopen_s(&fp, "A-large.in", "r", stdin);
	freopen_s(&fp, "output.txt", "w", stdout);
	int T; cin >> T;
	rep(cc, T) {
		string str; cin >> str;
		deque<char> q;
		q.push_back(str[0]);
		rep2(i, 1, str.size())
			if (q.front() > str[i])
				q.push_back(str[i]);
			else
				q.push_front(str[i]);
		string sol;
		rep(i, q.size())
			sol.push_back(q[i]);
		cout << "Case #" << cc + 1 << ": " << sol << endl;
	}
	return 0;
}