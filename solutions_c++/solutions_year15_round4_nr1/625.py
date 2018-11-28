#include<iostream>
#include<algorithm>
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

const int MAXN = 110;
const int MAXM = 0;
const int P = 1000000007;

// =====================================================
// Code goes here.
// main_solve() should return if it has seen EOF if (MULTI_TESTCASE && ! TESTCASE_NUM_GIVEN).
// The return value doesn't matter otherwise.

const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};

int n, m;
int a[MAXN][MAXN];
int p[MAXN * MAXN], v[MAXN * MAXN];

inline bool isValid( int i, int j ) {
	return 1 <= i && i <= n && 1 <= j && j <= m;
}

inline int GetNum( int i, int j ) {
	return j + (i - 1) * m;
}

int GetDest( int i, int j, int k ) {
	while ( 1 ) {
		i += dx[k], j += dy[k];
		if ( !isValid(i, j) )
			return 0;
		if ( a[i][j] != 4 )
			return GetNum(i, j);
	}
}

void sol() {
	int e[4];
	rep(i, 1, n)
		rep(j, 1, m) {
			if ( a[i][j] == 4 ) {
				p[ GetNum(i, j) ] = -1;
				continue;
			}
			bool fail = 1;
			rep(k, 0, 3) {
				e[k] = GetDest( i, j, k );
				if ( e[k] != 0 )
					fail = 0;
			}
			if ( fail ) {
				puts("IMPOSSIBLE");
				return;
			}
			p[ GetNum( i, j ) ] = e[ a[i][j] ];
		}
	int ans = 0;
	rep(x, 1, n * m)
		if ( p[x] == 0 )
			++ans;
	printf("%d\n", ans);
}
			

bool main_solve(){
	scanf("%d%d", &n, &m);
	rep(i, 1, n)
		rep(j, 1, m) {
			char c;
			while ( c = getchar(), c != '<' && c != '>' && c != 'v' && c != '^' && c != '.');
			int& f = a[i][j];
			if ( c == '.' )
				f = 4;
			else if ( c == '>' )
				f = 0;
			else if ( c == '^' )
				f = 1;
			else if ( c == '<' )
				f = 2;
			else if ( c == 'v' )
				f = 3;
			else
				puts("Unknown character!");
		}
	sol();
	return 0;
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
