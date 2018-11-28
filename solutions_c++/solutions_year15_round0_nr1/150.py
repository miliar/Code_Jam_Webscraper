#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
#include<assert.h>
using namespace std;
#define FOR(i,a,b) for(int i = a; i <= b; ++i)
#define FORD(i,a,b) for(int i = a; i >= b; --i)
#define RI(i,n) FOR(i,1,n)
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
bool debug;
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const ll INF = (ll) inf * inf;
const int nax = 1e6 + 5;

char sl[nax];

void te() {
	int n;
	scanf("%d", &n);
	++n;
	scanf("%s", sl);
	int juz = 0;
	int res = 0;
	REP(i, n) {
		int a = sl[i] - '0';
		if(a > 0 && juz < i) {
			res += i - juz;
			juz = i;
		}
		juz += a;
	}
	printf("%d\n", res);
}

int main(int argc, char *argv[])
{
	debug = argc > 1;
	
	int T;
	scanf("%d", &T);
	RI(test, T) {
		printf("Case #%d: ", test);
		te();
	}
	
	return 0;
}
