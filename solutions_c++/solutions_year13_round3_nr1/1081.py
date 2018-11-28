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


bool ok[256];

void init() {
	ok['a'] = ok['e'] = ok['i'] = ok['o'] = ok['u'] = true;
}

void Solve() {
	
	
	string s1;
	int r;
	cin >> s1 >> r;
	int n = SZ(s1);
	int res = 0;
	FOR(i,0,n) {
		FOR(j,1,n+1) {
			if(i+j>n)
				continue;
			string s = s1.substr(i,j);
			int row = 0;
			FOR(k,0,SZ(s)) {
				if(!ok[s[k]]) {
					row++;
					if(row >= r) {
						res++;
						break;
					}
				}
				else
					row = 0;
			}
		}
	}
	cout << res;
	cerr << res << " .. ";
}


int main() {
	clock_t begin = clock();
	init();



	freopen("a.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(CUR_TEST,1,test+1) {
		 
		printf("Case #%d: ",CUR_TEST);
		cerr << "Case #" << CUR_TEST << "...";
		Solve();
		cerr << "Done\n";
		printf("\n");
	}





	clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	cerr << "TIME: " << elapsed_secs << "\n";





	return 0;
}