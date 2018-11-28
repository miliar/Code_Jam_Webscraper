//BISM ILLAHHIRRAHMANNI RRAHIM

#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
using namespace std;

template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T sq(T x) { return x * x; }

#define ALL(p) p.begin(),p.end()
#define MP(x, y) make_pair(x, y)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define i64 long long
#define ld long double
#define pii pair< int, int >
#define psi pair< string, int >
#define vi vector< int >

const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;

int main() {
	//READ("input.in");
	//READ("A-small-attempt0.in");
	READ("A-small-attempt1.in");
	//READ("A-small-attempt2.in");
	//READ("A-small-attempt3.in");
	//READ("A-large.in");
	WRITE("A-2-output.out");
	int I,T;
	int fs,sc,i,j,u;
	cin>>T;
	for(I=1;I<=T;I++) {
		bool fl[17]={0};
		cin>>fs;
		fs--;
		for(i=0;i<4;i++) for(j=0;j<4;j++) {
			scanf("%d",&u);
			if(i==fs) fl[u]=1;
		}
		int cn=0,t=-1;
		cin>>sc;
		sc--;
		for(i=0;i<4;i++) for(j=0;j<4;j++) {
			scanf("%d",&u);
			if(i==sc && fl[u]) {
				cn++;
				t=u;
			}
		}
		printf("Case #%d: ",I);
		if(cn==1) cout<<t<<'\n';
		else if(cn==0) puts("Volunteer cheated!");
		else puts("Bad magician!");
	}
	return 0;
}
