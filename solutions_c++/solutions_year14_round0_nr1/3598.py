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


void Solve() {
	int r;
	cin >> r;
	r--;
	set<int> S;
	FOR(i,0,4) {
		vector<int> z(4);
		FOR(j,0,4) {
			cin >> z[j];
		}
		if(i==r) {
			S.insert(ALL(z));
		}
	}

	cin >> r;
	r--;

	VI ans;
	FOR(i,0,4) {
		vector<int> z(4);
		FOR(j,0,4) {
			cin >> z[j];
		}
		if(i==r) {
			FOR(j,0,4) {
				if(S.count(z[j])) {
					ans.PB(z[j]);
				}
			}
		}
	}
	switch(SZ(ans)) {
	case 1:
		cout << ans[0];
		break;
	case 0:
		cout << "Volunteer cheated!";
		break;
	default:
		cout << "Bad magician!";
		break;
	}
}


int main() {
	clock_t begin = clock();
	
	freopen("a.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(CUR_TEST,1,test+1) {
		 
		printf("Case #%d: ",CUR_TEST);
		cerr << "\tCase #" << CUR_TEST << "\n";
		Solve();
		printf("\n");
	}

	clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	cerr << "TIME: " << elapsed_secs << "\n";

	return 0;
}