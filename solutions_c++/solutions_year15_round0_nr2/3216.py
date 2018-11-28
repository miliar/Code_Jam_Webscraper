#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>

using namespace std;

#define rep(i,n) for((int)(i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define f first
#define s second
#define inf int(2e9)
#define sz(x) int((x).size())
#define sqr(x) (x) * (x)
#define all(x) (x).begin(), (x).end()

const double eps = 1e-9;
const double pi = acos(-1.0);
typedef long long ll;

int dp[1001], a[1001];

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);


	int T;
	cin >> T;
	
	for(int cs = 1; cs <= T; ++cs) {
	 	int ans = 1000, n;
	 	scanf("%d", &n);
	 	for(int i = 0; i < n; ++i) {
	 	 	scanf("%d", a + i);
	 	}

	 	for(int i = 1; i <= 1000; ++i) {
	 	 	int sum = 0;
	 	 	for(int j = 0; j < n; ++j)
	 	 		sum += (a[j] + i - 1) / i;
	 	 	ans = min(i + sum - n, ans);
	 	}

	 	printf("Case #%d: %d\n", cs, ans);
	}
	
	return 0; 
}