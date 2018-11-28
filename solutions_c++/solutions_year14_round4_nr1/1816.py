/**************************************************
 * Author	 : xiaohao Z
 * Blog	 : http://www.cnblogs.com/shu-xiaohao/
 * Last modified : 2014-05-31 21:51
 * Filename	 : 2014_R2_A.cpp
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
int a[LEN], n, m, f[LEN];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, kase = 1;
	cin >> T;
	while(T--){
		memset(f, 0, sizeof f);
		cin >> n >> m;
		for(int i=0; i<n; i++){
			cin >> a[i];
		}
		sort(a, a+n);
		int l = 0, r = n-1;
		while(l < r){
			if(a[l]+a[r] <= m) {
				l++; r--;
			}else {
				r--;
			}
		}
		int ans = n-l;
		cout << "Case #" << kase++ << ": " << ans << endl;
	}
	return 0;
}

