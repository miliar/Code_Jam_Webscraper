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
#define pii pair< i64, i64 >
#define psi pair< string, int >
#define vi vector< int >

const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;
#define MAXN 2200
#define MAXE 6200000
#define md 1000002013

int a[12000],b[12000],c[12000];

i64 ccst(i64 a,i64 n) {
	return n*a-((a*(a-1))>>1);
}

int main() {
	//READ("input.in");
	//READ("A-small-attempt0.in");
	//READ("A-small-attempt1.in");
	//READ("A-small-attempt2.in");
	//READ("A-small-attempt3.in");
	READ("A-large.in");
	WRITE("output_3.out");
	int I,T,m,i,n;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>n>>m;
		map < int , pii > v;
		map < int , pii > ::iterator it;
		i64 r=0;
		for(i=0;i<m;i++) {
			scanf("%d %d %d",&a[i],&b[i],&c[i]);
			v[a[i]].first+=c[i];
			v[b[i]].second+=c[i];
			r=(r+((ccst(b[i]-a[i],n)%md)*c[i])%md)%md;
		}
		stack < pii > st;
		i64 cs=0,t;
		for(it=v.begin();it!=v.end();it++) {
			if(it->second.first) st.push(pii(it->first,it->second.first));
			if(!(it->second.second)) continue;
			t=it->second.second;
			while(t>0) {
				if(t>=st.top().second) {
					t-=st.top().second;
					cs=(cs+(st.top().second*(ccst((it->first)-(st.top().first),n)%md))%md)%md;
					st.pop();
				}
				else {
					st.top().second-=t;
					cs=(cs+(t*(ccst((it->first)-(st.top().first),n)%md))%md)%md;
					t=0;
				}
			}
		}
		
		//cout<<r<<' '<<cs<<'\n';
		printf("Case #%d: %lld\n",I,(r-cs+md*2)%md);
	}
	return 0;
}
