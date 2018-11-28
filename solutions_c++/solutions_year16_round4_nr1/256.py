#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <utility>
#include <complex>

using namespace std;
typedef long long ll;
typedef double ld;

typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

string rps(int p, int r, int s, bool& okay){
	//cout << "r = " << r << ", s = " << s << ", p = " << p << endl;
	if(r + p < s) okay = false;
	if(r + s < p) okay = false;
	if(p + s < r) okay = false;
	if (!okay) return "";
	okay = true;
	if (r + p + s == 2){
		if (p == 0) return "RS";
		if (r == 0) return "PS";
		if (s == 0) return "PR";
	}
	string temp = rps((p+r-s)/2,(p+s-r)/2,(r+s-p)/2, okay);
	if (!okay) return "";
	string ans = "";
	for (int i = 0; i < temp.length(); i++){
		if (temp[i] == 'P') ans += "PR";
		if (temp[i] == 'R') ans += "PS";
		if (temp[i] == 'S') ans += "RS";
	}
	//cout << "r = " << r << ", s = " << s << ", p = " << p << ", ans = " << ans << endl;
	return ans;
}

int main(){
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		int n; cin >> n;
		int r, p, s; cin >> r >> p >> s;
		bool okay = true;
		string ans = rps(p,r,s,okay);
		if (!okay) cout << "Case #" << zz << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << zz << ": " << ans << endl;
	}
	
	return 0;
}
