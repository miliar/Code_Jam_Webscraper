#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iostream>
#include <iomanip>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef istringstream iss;
typedef ostringstream oss;

int main(){
	#ifndef ONLINE_JUDGE
 		freopen("B-small-attempt0.in", "r", stdin);
		freopen("vd.out", "w", stdout);
	#endif
	ios_base::sync_with_stdio(false);
	int t, a, b, k;
	cin >> t;
	for(int m = 1; m <= t; m++){
		long long res = 0;
		cin >> a >> b >> k;
		for(int i = 0; i < a; i++){
			for (int j = 0; j < b; j++){
				if ((i&j) < k) res++;
			}
		}
		cout << "Case #" <<  m <<  ": " << res << endl;
	}

	return 0;
}



