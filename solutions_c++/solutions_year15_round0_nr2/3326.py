#include<bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<__LINE__<<": "<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
const int inf = (int)1e9;
const double INF = 1e12, EPS = 1e-9;

int main(){
	int CS; cin >> CS;
	rep(cs, CS){
		int n;
		cin >> n;
		
		vi v(n);
		rep(i, n) cin >> v[i];
		
		int lo = 0, hi = 1010, mid;
		while(lo + 1 < hi){
			mid = (lo + hi) / 2;
			bool ok = 0;
			
			rep(mv, mid){
				
				int cnt = 0;
				rep(i, n){
					cnt += (v[i] + mid - mv - 1) / (mid - mv) - 1;
				}
				if(cnt <= mv){
					ok = 1;
					break;
				}
			}
			if(ok) hi = mid;
			else lo = mid;
		}
		
		printf("Case #%d: %d\n", cs + 1, hi);
	}
	return 0;
}