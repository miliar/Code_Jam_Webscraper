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

int N;
char str[1005];

void input(){
	scanf("%d%s", &N, str);
}
void solve(int t){
	int ret=0, sum=0;
	for (int i=0; i<=N; i++){
		if (sum < i){
			ret += i-sum;
			sum += i-sum;
		}
		sum += str[i] - '0';
	}
	printf("Case #%d: %d\n", t, ret);
}
int main(){
	int nT;
	scanf("%d", &nT);
	for (int t=1; t<=nT; t++){
		input();
		solve(t);
	}
	return 0;
}

