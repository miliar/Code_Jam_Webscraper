

#include <deque>
#include <queue>
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
#include <set>
#include <cstdlib>
#include <hash_map>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
#include <cstdlib>
#include <cassert>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define rep(i,s,e) for(int i=s;i<e;i++)
#define sz(X) ((int)(X.size()))
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
//---------------------------------------------------------------

#define maxn 1100000

int a[maxn];
LL sum[maxn];

int main() {
	freopen("F:/TDDOWNLOAD/A-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/A-large.out", "w", stdout);

	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++) {
		int N, p, q, r, s;
		cin>>N>>p>>q>>r>>s;
		for(int i=1;i<=N;i++) {
			a[i] = ((i-1)*(LL)p + q)%r + s;
			sum[i] = a[i] + sum[i-1];
		}
		sum[N+1] = sum[N];
		LL ma = 1LL<<50;

		for(int i=1;i<=N;i++) {
			int lo = i, hi = N;
			while(lo + 1 < hi) {
				int mid = (lo + hi) / 2;
				if((sum[mid]-sum[i-1])*2 < sum[N]-sum[i-1]) lo = mid;
				else hi = mid;
			}
			for(int j=lo-5;j<lo+5;j++) {
				if(j<i || j>N) continue;
				LL s1 = sum[i-1], s2 = sum[j]-sum[i-1], s3 = sum[N] - sum[j];
				ma = min(ma, max(s1, max(s2, s3)));
			}
		}
		//cout<<ma<<endl;
		printf("Case #%d: %.10lf\n", te, (sum[N]-ma)/(double)sum[N]);
	}
}








