/**************************************************
 * Author	 : xiaohao Z
 * Blog	 : http://www.cnblogs.com/shu-xiaohao/
 * Last modified : 2015-04-12 01:20
 * Filename	 : B.cpp
 * Description	 : 
 * ************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<unsigned int,unsigned int> puu;
typedef pair<int, double> pid;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;

const int INF = 0x3f3f3f3f;
const double eps = 1E-6;
const int LEN = 10010;
int num[LEN], M, n;

int J(int val) {
	int ret = 0;
	for(int i=0; i<n; i++) {
		ret += (num[i]/val - 1);
		if(num[i] % val) ret ++;
	}
//	cout << val << " | " << ret << endl;
	return val + ret;
}

int solve() {
	int l = 1, r = M;
	int ret = INF;
	for(int i=l; i<=r; i++) {
		ret = min(ret, J(i));
//		cout << i << ',' << J(i) << endl;
	}
	return ret;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, ans, kase = 1;
	scanf("%d", &T);
	while(T--){
		ans = M = 0;
		scanf("%d", &n);
		for(int i=0; i<n; i++){
			scanf("%d", &num[i]);
			M = max(M, num[i]);
		}
		ans = solve();
		printf("Case #%d: %d\n", kase ++, ans);
	}
	return 0;
}

