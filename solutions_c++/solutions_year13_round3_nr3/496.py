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


void init() {

}

void Solve() {
	int n;
	scanf("%d",&n);

	vector< pair<int, pair<PII,int> > > a;

	FOR(i,0,n) {
		int day, num, l, r, power, delta_d, delta_p, delta_s;
		scanf("%d%d%d%d%d%d%d%d", &day, &num, &l, &r, &power, &delta_d, &delta_p, &delta_s);
		while(num--) {
			a.PB( MP(day, MP( MP(l,r), power) ) );
			//process
			l += delta_p;
			r += delta_p;
			power += delta_s;
			day += delta_d;
		}
	}
	sort(ALL(a));
	VI wall(1000, 0);
	int res = 0;
	FOR(i,0,SZ(a))/*100*/{
		int start = i;
		VI nw = wall;
		while(i<SZ(a) && a[i].X==a[start].X) {
			int l = a[i].Y.X.X;
			int r = a[i].Y.X.Y;
			l *= 2;
			r *= 2;
			l += 500, r += 500;
			int power = a[i].Y.Y;
			bool ok = true;
			FOR(idx,l,r+1) {
				if(wall[idx] < power) {
					ok = false;
					nw[idx] = max(nw[idx], power);
				}
			}
			if(!ok)
				res ++;
			i++;
		}
		wall = nw;
		i--;
	}
	cout << res;
	cerr << res << endl;
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
		cerr << "\tCase #" << CUR_TEST << "\n";
		Solve();
		printf("\n");
	}





	clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	cerr << "TIME: " << elapsed_secs << "\n";





	return 0;
}