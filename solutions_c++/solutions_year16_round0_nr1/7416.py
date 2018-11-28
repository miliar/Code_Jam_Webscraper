#include <vector>
#include <queue>
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
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define fi first
#define se second
#define mp make_pair
#define sz(x) ((int)(x).size())
#define re return
#define pb(x) push_back(x)
#define pf(x) push_front(x)
#define abs(x) ((x) < 0 ? -(x) : (x))
#define INF 2000000000
#define sqr(x) ((x) * (x))
#define all(x) x.begin(), x.end()
#define fname "a"
#define MOD 1000000007

typedef long long ll;

int T, n, used[11], k, cnt = 1;

void process(int n) {
	while(n) {
		used[n % 10] = 1;
		n /= 10;
	}
}

bool ok() {
	for(int i = 0; i < 10; i++)
		if(!used[i]) return false;
	return true;
}
int main() {

	ios_base::sync_with_stdio(0);

	#ifndef ONLINE_JUDGE
		freopen("a.in", "r", stdin);
		freopen("a.txt", "w", stdout);
	#endif
	
	cin >> T;

	while(T--) {
		cin >> n;
		memset(used, 0, sizeof(int) * 10);
		if(n == 0) {
			printf("Case #%d: INSOMNIA\n", cnt);
		}
		else {
			int i = 1;
			while(1) {

				k = n * i;
				process(k);
				if(ok()) {
					printf("Case #%d: %d\n", cnt, k);
					break;
				}
				i++;
			}
		}
		cnt++;
	}
	return 0;
}







