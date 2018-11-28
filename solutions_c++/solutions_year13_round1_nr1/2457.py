#include <iostream>
#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)
#define pb push_back
#define FOREACH(x,y) for(typeof(y.begin()) x = y.begin() ; x != y.end() ; x++)

#define LL long long

LL MOD = 1000000007;

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tc;
	cin >> tc;
	for(int t = 1 ; t <= tc ; t++) {
		int r,n;
		cin >> r >> n;
		int ans = 1;
		int sum = 0;
		for(int i = 1 ; i < 1000 ; i++) {
			sum = sum + 2*r + 1;
			r = r + 2;
			if(sum <= n) {
				ans = i;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return (0);
}