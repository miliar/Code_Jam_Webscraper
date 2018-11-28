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
const i64 MOD = 1000000000 + 7;

i64 gcd(i64 a, i64 b) {
	return (a==0? b: gcd(b%a, a));
}

void Solve() {
	int n;
	cin >> n;
	VS s(n);
	FOR(i,0,n) {
		cin >> s[i];
	}
	
	vector<int> cnt(26, 0);
	
	vector<string> nodes;
	VS startAt(26, "");
	FOR(i,0,n) {
		if(s[i][0] == s[i].back()) {
			FOR(j,0,SZ(s[i])) {
				if(s[i][j]!=s[i][0]) {
					cout << 0;
					return ;
				}
			}
			cnt[s[i][0]-'a'] ++;
		}
		else {
			if(SZ(startAt[s[i][0]-'a']) == 0)
				startAt[s[i][0]-'a'] = s[i];
			else {
				cout << 0; 
				return ;
			}
			nodes.PB(s[i]);
		}
	}

	
	VI r(26, 0);
	FOR(i,0,SZ(nodes)) {
		r[nodes[i][0]-'a']++;
		r[nodes[i].back()-'a'] --;
	}

	int sumtmp = 0;
	int components = 0;
	bool ok = true;
	vector<string> ordered;

	FOR(i,0,26) {
		sumtmp += r[i];
		if(r[i]==1) components++;
		if(r[i] > 1) ok = false;
		if(r[i] < -1) ok = false;
	}
	
	if(sumtmp !=0)
		ok = false;
	if(!ok) {
		cout << 0;
		return ;
	}

	FOR(i,0,26) {
		if(r[i]==1) {
			//start from letter i+'a'
			string tmp = startAt[i];
			while(true) {
				ordered.PB(tmp);
				tmp = startAt[tmp.back() - 'a'];
				if(SZ(tmp) == 0)
					break;
			}
		}
	}

	if(SZ(ordered)!=SZ(nodes)) {
		cout << 0;
		return ;
	}

	FOR(i,0,26) {
		if(cnt[i]) {
			bool fixed = false;
			FOR(j,0,SZ(ordered)) {
				if(ordered[j][0]-'a' == i || ordered[j].back() -'a' == i)
					fixed = true;
			}
			if(!fixed) {
				ordered.PB(string(1,i+'a'));
				components ++;
			}
		}
	}

	vector<bool> was(26, false);
	string fstring = "";
	FOR(i,0,SZ(ordered)) {
		fstring += ordered[i];
	}
	FOR(i,0,SZ(fstring)) {
		if(was[fstring[i]-'a'] && fstring[i-1]!=fstring[i]) {
			ok = false;
		}
		was[fstring[i]-'a'] = true;
	}
	if(!ok) {
		cout << 0;
		return ;
	}

	i64 start = components;

	i64 res = 1;
	FOR(i,1,start+1) {
		res = res * i;
		res %= MOD;
	}

	FOR(i,0,26) {
		FOR(j,1,cnt[i]+1) {
			res = res * j;
			res %= MOD;
		}
	}
	cout << res;
}


int main() {
	clock_t begin = clock();
	
	freopen("a.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(CUR_TEST,1,test+1) {
		 
		printf("Case #%d: ",CUR_TEST);
		Solve();
		printf("\n");

		cerr << "\tCase #" << CUR_TEST << "\n";
	}

	clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	cerr << "TIME: " << elapsed_secs << "\n";

	return 0;
}