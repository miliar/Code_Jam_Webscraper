#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<string>
 
using namespace std;
 
#define s(n)                                 scanf("%d",&n)
#define sl(n)                                   scanf("%lld",&n)
#define sf(n)                                   scanf("%lf",&n)

#define EPS                                             1e-9
 
#define FOR(i,a,b)                              for(int i=a;i<b;i++)
#define REP(i,n)                                FOR(i,0,n)
#define foreach(v,c)            for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
 
#define mp                                              make_pair
#define pb                                              push_back
 
#define FF                                              first
#define SS                                              second
 
#define tri(a,b,c)                              mp(a,mp(b,c))
#define XX                                              first
#define YY                                              second.first
#define ZZ                                              second.second
 
/*Important ones*/
#define fill(a,v)                               memset(a,v,sizeof a)     //Works properly only for v = 0 or -1
#define all(x)                                  x.begin(),x.end()
 
#define SZ(v)                                   ((int)(v.size()))
#define DREP(a)                                 sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)                  (lower_bound(all(arr),ind)-arr.begin())
 
//typedefs. Use if you feel comfortable
typedef pair<int,int> PII;
typedef pair<long long,long long> PLL;
typedef pair< long long, PLL > TRI;

typedef vector<int> VI;
typedef long long LL;
typedef vector<LL> VL;
typedef vector<PII> VII;
typedef vector<PLL> VLL;
typedef vector<TRI> VT;
 
typedef vector<VI> VVI;
typedef vector<VL> VVL;
typedef vector<VII> VVII;
typedef vector<VLL> VVLL;
typedef vector<VT> VVT;

#define MAX 110

int grd[MAX][MAX], N, M, tests, row[MAX], col[MAX];

int main(){
	
	s(tests);
	FOR(testcase,0,tests){
		cout<<"Case #"<<testcase+1<<": ";
		s(N);	s(M);
		FOR(i,0,N)
			FOR(j,0,M)
				s(grd[i][j]);
		fill(row, 0);
		fill(col, 0);
		FOR(i,0,N)
			FOR(j,0,M){
				row[i] = max(row[i], grd[i][j]);
				col[j] = max(col[j], grd[i][j]);
			}
		int flag = 0;
		FOR(i,0,N){
			if(flag)
				break;
			FOR(j,0,M)
				if(grd[i][j] < row[i] && grd[i][j] < col[j]){
					cout<<"NO\n";
					flag = 1;
					break;
				}
		}
		if(!flag)
			cout<<"YES\n";
	}
	
	return 0;
	
}
