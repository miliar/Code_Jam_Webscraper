#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <string.h>
#include <ctime>
#include <limits.h>
using namespace std;

typedef long long ll;
const double pi=acos(-1.0);
const double eps=1e-11;
//const ll INF=(_I64_MAX)/2;
//#pragma comment(linker, "/STACK:102400000,102400000")
const int inf=0x3f3f3f3f;
#define maxx(a) memset(a, 0x3f, sizeof(a))
#define zero(a) memset(a, 0, sizeof(a))
template<class T>void show(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a, int r, int l){for(int i=0; i<r; ++i)show(a[i],l);cout<<endl;}
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define srep(i,n) for(i = 1;i <= n;i ++)
#define snuke(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MP make_pair
typedef pair<int,int > PII;

const int N = 1e5+ 111;
string s[12];
int main()
{
#ifndef ONLINE_JUDGE
   freopen("in.txt","r",stdin); 
   freopen("out.txt","w",stdout);
#endif
	int T,i,j,n;
	cin>>T;
	int cas = 1;
	while(T--){
		rep(i,4) cin>>s[i];
		printf("Case #%d: ",cas++);
		bool f = 0;
		rep(i,4){
			int tp = 0;
			rep(j,4){
				if(s[i][j] == 'X' || s[i][j] == 'T') tp ++;
			}
			if(tp == 4) f = 1;
		}
		bool g = 1;
		rep(i,4){
			if(s[i][i] != 'X' && s[i][i] != 'T') g = 0;	
		}
		if(g) f= 1;
		g = 1;
		rep(i,4){
			if(s[i][4-i-1] != 'X' && s[i][4-i-1] != 'T') g = 0;	
		}
		if(g) f= 1;
		rep(j,4){
			int tp = 0;
			rep(i,4){
				if(s[i][j] == 'X' || s[i][j] == 'T') tp ++;
			}
			if(tp == 4) f = 1;
		}
		if(f) {puts("X won");continue;}
		rep(i,4){
			int tp = 0;
			rep(j,4){
				if(s[i][j] == 'O' || s[i][j] == 'T') tp ++;
			}
			if(tp == 4) f = 1;
		}
		rep(j,4){
			int tp = 0;
			rep(i,4){
				if(s[i][j] == 'O' || s[i][j] == 'T') tp ++;
			}
			if(tp == 4) f = 1;
		}
		g = 1;
		rep(i,4){
			if(s[i][i] != 'O' && s[i][i] != 'T') g = 0;	
		}
		if(g) f= 1;
		g = 1;
		rep(i,4){
			if(s[i][4-i-1] != 'O' && s[i][4-i-1] != 'T') g = 0;	
		}
		if(g) f= 1;
		if(f) {puts("O won");continue;}
		rep(i,4) rep(j,4) if(s[i][j] == '.') f = 1;
		if(f) {puts("Game has not completed");}
		else puts("Draw");
	}	

return 0;
}