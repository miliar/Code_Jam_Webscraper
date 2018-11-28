#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <bitset>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <fstream>
#include <tuple>
#include <set>
#include <functional> 
#include <string.h>
//#include <assert.h>
//#include <typeinfo.h>
#include <time.h>

#define X first
#define Y second
#define MP make_pair
#define MT make_tuple
#define FOR(i, n) for(int (i) = 0; (i) < (n); ++(i))
#define REP(i, a, n) for(int (i) = (a); (i) < (n); ++(i))
typedef long long ll;
typedef std::pair<int, int> pii;
typedef std::pair<ll, ll > pll;
using namespace std;

const int INIT_SIZE_MAX = (1 << 29) + 10;
const int INIT_SIZE_MIN = -(1 << 29) - 10;
const int INIT_SIZE = 0;
const int MAX = 8;
const int DIR_SIZE = 12;
const double PI = 3.1415926535897932384;

template<class T, class U>
void convert(T &t, U &u){
	stringstream ss;
	ss << t;
	ss >> u;
}

int main(){
	int n; cin >> n;

	for (int i = 1; i <= n; ++i){
		int a, b, m; cin >> a >> b >> m;
		
		ll ans = 0;
		for (int j = 0; j < a; ++j){
			for (int k = 0; k < b; ++k){ 
				if ((j & k) < m) ++ans;
			}
		}

		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}