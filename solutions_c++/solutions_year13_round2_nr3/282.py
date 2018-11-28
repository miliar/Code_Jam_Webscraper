//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#define _CRT_SECURE_NO_DEPRECATE
#include<sstream>
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<complex>
#include<set>
#include<algorithm>
#include<ctime>

using namespace std;

typedef unsigned long long      ui64;
typedef long long               i64;
typedef	vector<int>             VI;
typedef	vector<bool>            VB;
typedef	vector<VI>              VVI;
typedef	vector<string>          VS;
typedef	pair<int,int>           PII;
typedef map<string,int>         MSI;
typedef set<int>                SI;
typedef set<string>             SS;
typedef complex<double>         CD;
typedef vector< CD >            VCD;
typedef map<int,int>            MII;
typedef	pair<double,double>     PDD;

#define PB                      push_back
#define MP                      make_pair
#define X                       first
#define Y                       second
#define FOR(i, a, b)            for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b)           for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b)             memset(a, b, sizeof(a))
#define SZ(a)                   int((a).size())
#define ALL(a)                  (a).begin(), (a).end()
#define RALL(a)                 (a).rbegin(), (a).rend()
#define INF                     (2000000000)

#ifdef _DEBUG
#define eprintf(...) fprintf (stderr, __VA_ARGS__)
#else
#define eprintf(...) assert (true)
#endif

const double PI = acos(-1.0);

const int lib_s = 521196;
string lib[lib_s];

const int MAXN = 50;
char buf[MAXN];

pair<int,PII> can(string s1, string s2) {
	//score, last
	int res = 0;
	int last = -INF;
	int first = INF;
	FOR(i,0,SZ(s1)) {
		if(s1[i]!=s2[i]) {
			if(i - last < 5)
				return MP( -1,MP(-1,-1) );
			last = i;
			first = min(first, i);
			res++;
		}
	}
	return MP(res, MP(min(4, first), min(4, SZ(s1) - last - 1) ) );
}

void Solve() {
	string s;
	scanf("%s",buf);
	s = buf;
	VVI dp(SZ(s) + 1, VI(5,INF) );
	FOR(i,0,5)
		dp[0][i] = 0;
	FOR(i,0,SZ(s)) {
		FOR(j,0,lib_s) {
			string word = lib[j];
			if(SZ(word) > i+1)
				continue;
			pair<int,PII> Pair = can(word, s.substr(i+1-SZ(word),SZ(word)));
			int val = Pair.X;
			if(val == -1)
				continue;
			int f = Pair.Y.X; 
			int l = Pair.Y.Y;
			FOR(k,0,5) {
				if(f + k + 1 >= 5) {
					int tmp_last = min(l, SZ(word) + k);
					dp[i+1][tmp_last] = min( dp[i+1][tmp_last], dp[i+1-SZ(word)][k] + val );
				}
			}
		}
	}
	int res = INF;
	FOR(i,0,5)
		res = min(res, dp[SZ(s)][i]);
	cerr << res << " :: ";
	printf("%d",res);
}


int main() {
	clock_t begin = clock();
	freopen("garbled_email_dictionary.txt","r",stdin);
	FOR(i,0,lib_s) {
		scanf("%s",buf);
		lib[i] = buf;
	}
	fclose(stdin);
	freopen("a.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(CUR_TEST,1,test+1) {
		 
		printf("Case #%d: ",CUR_TEST);
		Solve();
		cerr << "Case #" << CUR_TEST << ";\n";
		printf("\n");
	}
	clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	cerr << "TIME: " << elapsed_secs << "\n";
	return 0;
}