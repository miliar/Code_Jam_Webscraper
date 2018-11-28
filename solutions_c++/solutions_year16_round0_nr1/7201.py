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

set<int> ten;
bool judge2(long long tmp) {
	//if (tmp != 0 && tmp % 10 == 0) ten.insert(0);
	for (; tmp; tmp /= 10)
		ten.insert(tmp % 10);
	if (ten.size() == 10) return true;
	else return false;
}
long long judge(long long n) {
	if (n == 0) return 0;
	long long ret = 1;
	while (true) {
		long long tmp = n * ret;
		bool ok = judge2(tmp);
		if (ok) break;
		ret++;
	}
	return ret;
}

int main() {
	FILE* fp;
	freopen_s(&fp, "A-large.in", "r", stdin);
	freopen_s(&fp, "output.txt", "w", stdout);

	int T; cin >> T;
	rep(cc,T) {
		ten.clear();
		long long N;
		cin >> N;
		long long sol = judge(N);
		if (sol == 0)
			cout << "Case #" << cc + 1 << ": INSOMNIA" << endl;
		else
			cout << "Case #" << cc + 1 << ": " << sol * N << endl;
	}

	return 0;
}