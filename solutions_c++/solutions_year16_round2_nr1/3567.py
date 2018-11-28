#include <queue>
#include <iostream>       
#include <string>
#include <vector>
#include <fstream>        
#include <functional> 
#include <algorithm>  //min, max, sort
#include <cstdlib>    
#include <cstring>    //memset
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
const int INF = 987654321;
string num[10];
int my[26];
string str;
vi sol;
void setting() {
	num[0] = "ZERO";
	num[1] = "ONE";
	num[2] = "TWO";
	num[3] = "THREE";
	num[4] = "FOUR";
	num[5] = "FIVE";
	num[6] = "SIX";
	num[7] = "SEVEN";
	num[8] = "EIGHT";
	num[9] = "NINE";
}
bool sett(int index, int dt) {
	bool ok = true;
	rep(i, num[index].size()) {
		my[num[index][i] - 'A'] += dt;
		if (my[num[index][i] - 'A'] < 0) 
			ok = false;
	}
	return ok;
}
bool rec(int here) {
	if (here == str.size()) return true;
	if (here > str.size()) return false;
	rep(i, 10) {
		if (sett(i, -1))
			if (rec(here + num[i].size())) {
				sol.push_back(i);
				return true;
			}
		sett(i, +1);
	}
	return false;
}
int main() {
	setting();
	FILE *fp;
	//freopen_s(&fp, "input.in", "r", stdin);
	freopen_s(&fp, "A-small-attempt0.in", "r", stdin);
	freopen_s(&fp, "output.txt", "w", stdout);
	int T; cin >> T;
	rep(cc, T) {
		cin >> str;
		memset(my, 0, sizeof(my));
		sol.resize(0);
		rep(i, str.size()) my[str[i] - 'A']++;
		
		bool ok = rec(0);
		sort(sol.begin(), sol.end());
		cout << "Case #" << cc + 1 << ": ";
		rep(i, sol.size()) cout << sol[i];
		cout << endl;
		int debug; 
		debug = 3;
	}
	return 0;
}