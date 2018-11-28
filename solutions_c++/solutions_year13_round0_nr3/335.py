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

const int MAXN = 100 + 7;
int a[MAXN][MAXN];

i64 good[39] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};

void Solve() {
	i64 a, b;
	scanf("%lld%lld",&a,&b);
	int res = 0;
	FOR(i,0,39) {
		if(good[i]>=a && good[i] <= b)
			res++;
	}
	printf("%d",res);
}




bool pal(i64 a) {
	i64 res= 0;
	i64 back = a;
	while(a) {
		res = res  * 10ll + a%10;
		a /= 10;
	}
	return back == res;
}


int main() {/*
	cout << good[38] << endl;
	return 0;
	vector<i64> res;
	FOR(i,0,10000001) {
		if( pal(i) && pal(1ll*i*i) )
			res.PB(1ll*i*i);
	}
	cout << SZ(res) << endl;
	FOR(i,0,SZ(res))
		cout << res[i] << ", ";
	return 0;
	*/
	freopen("a.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test;
	scanf("%d",&test);
	FOR(CUR_TEST,1,test+1) {
		printf("Case #%d: ",CUR_TEST);
		Solve();
		printf("\n");
	}
	return 0;
}