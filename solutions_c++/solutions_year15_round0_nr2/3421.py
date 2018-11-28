/*************
	Team - ThePrestige
****************/
#include <climits>
#include <queue>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <cassert>

using namespace std;

#define rep(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define ll long long int
#define ii pair<int,int>
#define gi(x) scanf("%d",&x)
#define gl(x) scanf("%lld",&x)
#define Clear(x,val) memset(x,val,sizeof(x))
#define SZ(v) (v).size()
#define MAX 1007
#define eps 1e-9

int pc_orig[MAX];

int main() {
	int T; cin >> T;
	rep(i, 0, T) {
		int N; cin >> N;
		Clear(pc_orig, 0);
		rep(i, 0, N) {
			int x;cin >> x;
			pc_orig[x] ++;
		}

		int ans = 10 * MAX;
		rep(i, 1, MAX) {
			int inturpt = 0;
			rep(j, i+1, MAX) {
				if (pc_orig[j]) {
					inturpt += (pc_orig[j]) * ((j/i) - 1);	
					if(j%i) inturpt += (pc_orig[j]);
				}
			}
			ans = min(ans, inturpt+i);
		}
		cout << "Case #" << i+1 << ": " << ans << "\n";
	}
	return 0;
}
