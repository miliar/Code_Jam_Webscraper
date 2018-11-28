//bcw0x1bd2 {{{
#include<bits/stdc++.h>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define MC(n,m) memcpy((n),(m),sizeof(n))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define FOR(x,y) for(__typeof(y.begin())x=y.begin();x!=y.end();x++)
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
#ifdef ONLINE_JUDGE
#define FILEIO(name) \
  freopen(name".in", "r", stdin); \
  freopen(name".out", "w", stdout);
#else
#define FILEIO(name)
#endif

void RI() {}

template<typename... T>
void RI( int& head, T&... tail ) {
	    scanf("%d",&head);
			    RI(tail...);
}

mt19937 rng(0x5EED);
int randint(int lb, int ub) {
    return uniform_int_distribution<int>(lb, ub)(rng);
}
// Let's Fight! }}}

int N, ip[1024];

bool check(int c, int tm){
	for (int i=N-1; i>=0 && ip[i] > tm; i--){
		int tmp = (ip[i]-1) / tm;
		c -= tmp;
		if (c < 0) return false;
	}
	return true;
}
void solve(int t){
	scanf("%d", &N);
	for (int i=0; i<N; i++)
		scanf("%d", &ip[i]);
	sort(ip,ip+N);
	int ret = ip[N-1];
	for (int c=1; c<=ret; c++){
		int l=1, r=ret+1;
		while (l<r){
			int mid = (l+r)/2;
			if (check(c,mid)) r=mid;
			else l = mid+1;
		}
		if (check(c, l))
			ret = min(ret, l+c);
	}
	printf("Case #%d: %d\n", t, ret);
}
int main(){
	int nT;
	scanf("%d", &nT);
	for (int t=1; t<=nT; t++)
		solve(t);
	return 0;
}

