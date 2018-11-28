#include <bits/stdc++.h>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;
#define XINF INT_MAX
#define INF 0x3F3F3F3F
#define MP(X,Y) make_pair(X,Y)
#define PB(X) push_back(X)
#define REP(X,N) for(int X=0;X<N;X++)
#define REP2(X,L,R) for(int X=L;X<=R;X++)
#define DEP(X,R,L) for(int X=R;X>=L;X--)
#define CLR(A,X) memset(A,X,sizeof(A))
#define IT iterator
#define RIT reverse_iterator
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<int> VI;
typedef tree<int, int, greater<int>, rb_tree_tag, tree_order_statistics_node_update > rb_tree;
#define ALL(X) (X).begin(),(X).end()
#define PQ std::priority_queue
#define HEAP __gnu_pbds::priority_queue
#define X first
#define Y second
#define lson(X) ((X)<<1)
#define rson(X) ((X)<<1|1)

string gao(string a, string b) {
	if(a < b) return a + b;
	else return b + a;
}

string ans[13][3];
int c[13][3][3];

int main()
{
#ifdef LOCAL
	   freopen("A-large.in","r",stdin);
	   freopen("A-large.out","w",stdout);
#endif
	ios::sync_with_stdio(false);
	int t,cs=1;
	ans[0][0] = "P";
	ans[0][1] = "R";
	ans[0][2] = "S";
	
	REP2(i,0,11) {
		REP(j,3)
			ans[i+1][j] = gao(ans[i][j], ans[i][(j+1)%3]);
	}
	REP2(i,0,12) {
		REP(j,3) {
			REP(k,ans[i][j].size()) {
				if(ans[i][j][k] == 'P') c[i][j][0]++;
				if(ans[i][j][k] == 'R') c[i][j][1]++;
				if(ans[i][j][k] == 'S') c[i][j][2]++;
			}
		}
	}
	cin>>t;
	while(t--) {
		int n,p,r,s;
		cin>>n>>r>>p>>s;
		
		
		cout<<"Case #"<<cs++<<": ";
		string res = "d";
		REP(i,3) {
			if(c[n][i][0] == p && c[n][i][1] == r) {
				res = min(res, ans[n][i]);
			}
		}
		
		if(res[0] == 'd') {
			cout<<"IMPOSSIBLE"<<endl;
		}else{
			cout<<res<<endl;
		}
	}
	return 0;
}


