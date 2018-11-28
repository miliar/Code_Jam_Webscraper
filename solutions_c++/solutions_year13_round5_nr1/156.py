#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
using namespace std;
#define pb push_back
#define INF 1000000000
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define mp make_pair
#define pii pair<int,int>
#define ll long long
#define vi vector<int>
#define SZ(x) ((int)(x.size()))
#define fi first
#define se second
#define wez(n) int (n); scanf("%d",&(n));
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
inline void pisz(int n) { printf("%d\n",n); }
template<typename T,typename TT> ostream& operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream& operator<<(ostream &s,vector<T> t){FOR(i,SZ(t))s<<t[i]<<" ";return s; }
#define IN(x,y) ((y).find((x))!=(y).end())
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define TESTS wez(testow)while(testow--)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define IOS ios_base::sync_with_stdio(0);

long long x[44];
long long y[44];

double test() {
	long long b;
	int n;
	scanf("%lld%d", &b, &n);
	FOR(i,38) x[i]=0;
	FOR(i,n) scanf("%lld", &x[i+37-n]);
	sort(x+37-n,x+37);
	x[37] = 1e14;
	double best = 0;
	FORI(take,37) {
		//printf("best = %lf, ", best);
		long long cur = b;
		long long res = 0;
		FOR(i,38) y[i] = x[i];
		if (y[take] == y[take-1]) {
			int j = take;
			while (y[j] == y[take-1]) {
				y[j]++;
				cur--;
				j++;
			}
		}
		bool wrong = false;
		long long dest = y[take-1];
		FOR(i,take) {
			if (cur + y[i] < dest) {
				wrong = true;
			}
			cur -= dest - y[i];
			res += dest - y[i];
			y[i] = dest;
		}
		if (wrong) continue;
		long long add = cur / take;
		//printf("take = %d, add = %lld, ", take, add);
		if (dest + add < y[take]) {
			res += add * take;
			cur -= add * take;
			//printf("res = %lld, cur = %lld, try = %lf\n", res, cur, 36.0 * res / take - b + cur);
			best = max(best, 36.0 * res / take - b + cur);
			continue;
		}
		FOR(i,take) y[i] = y[take]-1;
		cur -= take * (y[take]-1-dest);
		res += take * (y[take]-1-dest);
		int last = take;
		while (y[last] == y[take]) last++;
		while (cur > 0) {
			long long add = cur / last;
			//printf("add = %lld, ", add);
			if (y[0] + add < y[last]) {
				res += add * take;
				cur -= add * last;
				//printf("res = %lld, try = %lf\n", res, 36.0 * res / take - b + cur);
				best = max(best, 36.0 * res / take - b + cur);
				break;
			}
			add = y[last] - y[take];
			FOR(i,last) y[i] += add;
			cur -= add * last;
			res += add * take;
			while (y[last] == y[take]) last++;
		}
	}
	return best;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; tt++) {
		printf("Case #%d: %.7lf\n", tt, test());
	}
	return 0;
}
