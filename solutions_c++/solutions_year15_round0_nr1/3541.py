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

const int ZERO = 48;

int main() {
	int T; cin >> T;
	rep(i, 0, T) {
		int smax; string shy;
		cin >> smax >> shy;
		int arr[MAX];Clear(arr, 0);
		int ans = 0, standing = 0;
		rep(i, 0, shy.size()) {
			int people = (int)shy[i] - ZERO;
			if (people) {
				if (i <= standing) standing += people;
				else {
					int need = i - standing;
					ans += need;
					standing += (need + people);
				}
			}
		}	
		cout << "Case #" << i+1 << ": " << ans << "\n";
	}
	return 0;
}
