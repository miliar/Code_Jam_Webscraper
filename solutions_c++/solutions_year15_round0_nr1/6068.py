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
#define root 1
#define lft 2*idx
#define rgt 2*idx+1
#define cllft lft,st,mid
#define clrgt rgt,mid+1,ed
#define i64 long long
#define ld long double
#define pii pair< int, int >
#define psi pair< string, int >
#define MX 1002

const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;
char a[MX], b[MX];

int main() {
	// READ("A-large.in");
	// WRITE("Output.txt");
	int t;
	scanf("%d",&t);
	int max = t;
	while(t--){
		CLR(a);
		CLR(b);
		int smax;
		scanf("%d",&smax);
		scanf("%s",a);
		long long int needed=0,have=0,i=1,diff=0;
		have = a[0]-'0';
		while(i<=smax){
			if (i<=have)
			{
				//more will stand so add a[i] to have
				have+=a[i]-'0';
				i++;
			}else{
				//we will need more to make ishyed ppl stand so increase have and needed by diff
				diff = i - have;
				have += diff;
				needed +=diff;
			}
		}
		printf("Case #%d: %d\n",max-t,needed);
	}
	return 0;
}
