//#pragma comment(linker,"/STACK:16777216") /*16Mb*/
//#pragma comment(linker,"/STACK:33554432") /*32Mb*/
#include<sstream>
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include <time.h>
#include<cmath>
#include<memory>
#include<memory.h>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long      ULL;
typedef long long               LL;

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
#define INF                     (1000000000)
#define FILL                    CLEAR

const int MOD = 1000002013;

void submit(){
	freopen("in.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
}

LL f(LL a , LL steps , LL p){
	LL t1 = steps * a % MOD;
	LL t2 = (steps * (steps - 1)) / 2 % MOD;
	LL t = (t1 - t2 + MOD) % MOD;
	return t * p % MOD;
}

int main()
{
	submit();

	int t;
	cin >> t;
	FOR(test,0,t){
		cout << "Case #" << test + 1 << ": ";
		LL n;
		int m;
		cin >> n >> m;
		LL res = 0;
		vector<pair<LL , pair<int , LL > > > a;
		LL MM = 0;
		for(int i = 0; i < m; ++i){
			int b, e, p;
			cin >>  b >> e  >> p;
			MM += f(n , e - b , p);
			MM %= MOD;
			a.PB(MP(b , MP(0 , p)));
			a.PB(MP(e , MP(1 , p)));
		}
		sort(ALL(a));
		vector<pair<LL,LL> > c;
		for(int i = 0; i < 2 * m - 1; ++i){
			if (a[i].second.first == 0){
				c.push_back(MP(n , a[i].second.second));
			}
			else{
				int k = a[i].second.second;
				while (k > 0){
					if (c[c.size() - 1].second > k){
						c[c.size() - 1].second -= k;
						k = 0;
					}
					else{
						k -= c[c.size() - 1].second;
						c.pop_back();
					}
				}
			}
			sort(ALL(c));
			LL steps = a[i + 1].first - a[i].first;
			
			FOR(j,0,c.size()){
				res += f(c[j].first , steps , c[j].second);
				c[j].first -= steps;
			}

			res %= MOD;
		}
				
		cout << (MM - res + MOD) % MOD << endl;			
	}

    return 0;
};