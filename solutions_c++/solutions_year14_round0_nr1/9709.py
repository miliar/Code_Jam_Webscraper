#define TRACE
#define DEBUG

#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<string> vs;
typedef vector<ii> vii;

// Basic macros
#define fst first
#define snd second
#define all(x) (x).begin(), (x).end()
#define clr(a, v) memset(a, v, sizeof(a))
#define FOR(i,s,n) for(int i=s;i<(n);i++)
#define REP(i,n) FOR(i,0,n)
#define FORV(i,f,t) for(int i = f; i >= t; --i)
#define REPV(i,n) FORV(i,n,0)
#define pb push_back
#define mp make_pair
#define sz(x) (int)(x.size())

//in-out macros

#define si(x) scanf("%d",&x)
#define ci(x) cin>>x
#define sd(x) scanf("%lf",&x)
#define ss(x) scanf("%s",x)
#define gc(x) c=getchar()

#define pis(x) printf("%d ",x)
#define pin(x) printf("%d\n",x)
#define pls(x) cout<<x<<" "
#define pln(x) cout<<x<<endl
#define pds(x) printf("%.12f ",x)
#define pdn(x) printf("%.12f\n",x)
#define pnl()  printf("\n")


const int oo = 2000000009;
const double eps = 1e-9;

#ifdef TRACE
#define trace1(x) cerr << #x << ": " << x << endl;
#define trace2(x, y) cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)

#endif

int mat[4][4];
int ava;
int curr;

int main(){
	int T; si(T);
	FOR(cas,1,T+1){
		int row;
		si(row);
		ava=curr=0;
		REP(i,4){
			REP(j,4){
				si(mat[i][j]);
				if(i==row-1) (curr|=(1<<mat[i][j]));
			}
		}
		ava=curr;
		curr=0;
		si(row);
		REP(i,4){
			REP(j,4){
				si(mat[i][j]);
				if(i==row-1) (curr|=(1<<mat[i][j]));
			}
		}
		ava&=curr;
		if(__builtin_popcount(ava)==0) printf("Case #%d: Volunteer cheated!\n",cas);
		else if(__builtin_popcount(ava)>1) printf("Case #%d: Bad magician!\n",cas);
		else{
			int i=0;
			while(!(ava&(1<<i)))i++;
			printf("Case #%d: %d\n",cas,i);
		}
	}
	return 0;
}
