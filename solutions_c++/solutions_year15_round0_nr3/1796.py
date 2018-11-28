#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <math.h>
#include <utility>
#include <iterator>
#include <fstream>
#include <cstdio>
#include <functional>
#include <cassert>
#include <array>

using namespace std;

template<class T>
string tostring(T a){ stringstream ss; ss << a; return ss.str(); }

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> II;
#define SZ(a) int((a).size()) 
#define PB push_back 
#define ALL(c) (c).begin(),(c).end() 
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])

using quat = pair < char, char > ;

quat tab(char a, char b){
	//if(a == '' && b == '') return make_pair(, '');
	if(a == '1' && b == '1') return make_pair(+1, '1');
	if(a == '1' && b == 'i') return make_pair(+1, 'i');
	if(a == '1' && b == 'j') return make_pair(+1, 'j');
	if(a == '1' && b == 'k') return make_pair(+1, 'k');
	if(a == 'i' && b == '1') return make_pair(+1, 'i');
	if(a == 'i' && b == 'i') return make_pair(-1, '1');
	if(a == 'i' && b == 'j') return make_pair(+1, 'k');
	if(a == 'i' && b == 'k') return make_pair(-1, 'j');
	if(a == 'j' && b == '1') return make_pair(+1, 'j');
	if(a == 'j' && b == 'i') return make_pair(-1, 'k');
	if(a == 'j' && b == 'j') return make_pair(-1, '1');
	if(a == 'j' && b == 'k') return make_pair(+1, 'i');
	if(a == 'k' && b == '1') return make_pair(+1, 'k');
	if(a == 'k' && b == 'i') return make_pair(+1, 'j');
	if(a == 'k' && b == 'j') return make_pair(-1, 'i');
	if(a == 'k' && b == 'k') return make_pair(-1, '1');
}

quat mul(quat a, quat b){
	quat t = tab(a.second, b.second);
	return make_pair(a.first * b.first * t.first, t.second);
}

int main(){
	ifstream be("C-small-attempt0.in");
	ofstream ki("ki.txt");
	int T;
	be >> T;
	FOR(tt, T){
		int l, x; be >> l >> x;
		string s0; be >> s0;
		assert(SZ(s0) == l);
		stringstream ss;
		FOR(i, x){
			ss << s0;
		}
		string s = ss.str();
		int n = SZ(s);
		assert(n == l*x);

		vector<vector<quat>> dp(n + 1, vector<quat>(n + 1));
		FOR(i, n + 1){
			pair<char, char> u{ 1, '1' };
			dp[i][i] = u;
			for(int j = i + 1; j < n + 1; j++){
				dp[i][j] = mul(dp[i][j - 1], quat{ 1, s[j - 1] });
			}
		}

		bool ok = false;
		for(int i = 1; i < n; i++){
			if(dp[0][i] == quat{ 1, 'i' }){
				for(int j = i; j < n - 1; j++){
					if(
						dp[i][j + 1] == quat{ 1, 'j' } &&
						dp[j + 1][n] == quat{ 1, 'k' }){
						ok = true;
						break;
					}
				}
				if(ok)
					break;
			}
		}
		cout << tt << endl;
		ki << "Case #" << tt + 1 << ": " << (ok ? "YES" : "NO") << endl;
	}


	ki.close();
	return 0;
}