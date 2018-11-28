#include<iostream>
#include<algorithm>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<string>
#include<cstdio>
#include<cstring>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

#define mp make_pair
#define X first
#define Y second

#define pb push_back
#define forI_(i,V,_) for(__typeof(V.end())i=_;i!=V.end();++i)
#define forI(i,V) forI_(i,V,V.begin())

#define rep(i,l,r) for(int i = l; i <= r; ++i)
#define per(i,r,l) for(int i = r; i >= l; --i)
#define rep_(i,l,r) for(int i = l; i < r; ++i)
#define per_(i,r,l) for(int i = r; i > l; --i)

// =====================================================
// Settings

string prob = "t";

const int OUTPUT_TO_FILE = 0;
const int MULTI_TESTCASE = 1;
const int TESTCASE_NUM_GIVEN = 1;
const int OUTPUT_CASE_NUM = 1;

const int MAXN = 3000;
const int MAXM = 0;
const int P = 1000000007;

// =====================================================
// Code goes here.
// main_solve() should return if it has seen EOF if (MULTI_TESTCASE && ! TESTCASE_NUM_GIVEN).
// The return value doesn't matter otherwise.

map<string, int> G;
vector<int> v[MAXN];
bool f[3][MAXN], g[3][MAXN];

int m;

inline int GetNum ( const string & s ) {
	if ( G.find( s ) == G.end() )
		G[s] = ++m;
	return G[s];
}

bool main_solve(){
	int n;
	scanf("%d\n", &n);
	m = 0;
	G.clear();
	rep(i, 1, n) {
		string s;
		getline( cin, s );
		//cout << "getline : " << s << endl;
		v[i].clear();
		istringstream iss( s );
		string t;
		while ( iss >> t ) {
			//cout << "read : " << t << " " << GetNum( t ) << endl;
			v[i].pb( GetNum( t ) );
		}
		//cout << "read : finish a line" << endl;
	}
	/*rep(j, 1, n) {
		forI(i, v[j])
			printf("%d ", *i);
		puts("");
	}*/
	rep(i, 1, m)
		f[1][i] = f[2][i] = 0;
	rep(j, 1, 2)
		forI(i, v[j])
			f[j][*i] = 1;
	/*puts("initial");
	rep(j, 1, 2) {
		rep(i, 1, m)
			printf("%d ", f[j][i]);
		puts("");
	}*/
	int all = 1 << (n - 2);
	int ans = m;
	rep(s, 0, all - 1) {
		rep(i, 1, m)
			rep(j, 1, 2)
				g[j][i] = f[j][i];
		rep(i, 3, n) {
			int t = ( ( s >> ( i - 3 ) ) % 2 ) + 1;
			//printf("assigning line %d to %d\n", i, t);
			forI(it, v[i]) {
				g[t][*it] = 1;
				//printf("--- assign %d to %d\n", *it, t);
			}
		}
		/*puts("--- g");
		rep(j, 1, 2) {
			rep(i, 1, m)
				printf("%d ", g[j][i]);
			puts("");
		}*/
		int t = 0;
		rep(i, 1, m)
			if ( g[1][i] && g[2][i] )
				++t;
		//printf("t = %d\n", t);
		ans = min(ans, t);
	}
	cout << ans << endl;
}

// =====================================================

int main(){
#ifdef ONLINE_JUDGE
	if(prob == "t")
		prob = "";
#endif
	if(prob != ""){
		freopen((prob+".in").c_str(), "r", stdin);
		if(OUTPUT_TO_FILE)
			freopen((prob+".out").c_str(), "w", stdout);
	}
	if(MULTI_TESTCASE){
		if(TESTCASE_NUM_GIVEN){
			int TC;
			scanf("%d\n", &TC);
			rep(T, 1, TC){
				if(OUTPUT_CASE_NUM)
					printf("Case #%d: ", T);
				main_solve();
			}
		}else{
			while(main_solve());
		}
	}else{
		main_solve();
	}
	return 0;
}
