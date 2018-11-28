#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
#define FOR(i,a,n) for(int i=a;i<(int)(n);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),(a).end()
#define MP(a,b) make_pair(a,b)
#define PB(a) push_back(a)
#define F first
#define S second
const int INF = 2000000000;
const int DX[4]={0,1,0,-1}, DY[4]={-1,0,1,0};
struct P{int x;int y;P(int X=0,int Y=0){x=X;y=Y;}};

ll mx(ll a, ll b) {
	return (a > b ? a : b);
}

int main() {
	int T;
	cin >> T;
	REP(t,T) {
		int n;
		cin >> n;
		vector<ll> m(n);
		REP(i,n) cin >> m[i];

		ll y=0,z=0;
		ll s=0;
		FOR(i,1,n) {
			y += mx(0, m[i-1] - m[i]);
			s = mx(s,m[i-1]-m[i]);
		}

		FOR(i,0,n-1) {
			z += (m[i]>s ? s : m[i]);
		}
		printf("Case #%d: %lld %lld\n",t+1,y,z);
	}
	return 0;
}
