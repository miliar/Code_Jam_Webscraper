#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
#define int long long
#undef int
int main()
{
#define int long long
	ios_base::sync_with_stdio(0);
#define name "B-large (1)"
	freopen(name ".in","r",stdin);
	freopen(name ".out","w",stdout);
	int t;
	cin>>t;
	REP(q,t){
		int k;
		cin>>k;
		vector<int> a;
		REP(i, k){
			int temp;
			cin>>temp;	
			a.PB(temp);
		}
		int best = 1e9;
		int offset = 0;
		for(int i = 1; i <= 1000; i++){
			int score = i;
			REP(j, a.size()){
				score += ceill((long double)a[j] / (long double)i) - 1;
			}
			best = min(best, score);
		}
		cout<<"Case #"<<q + 1<<": "<<best<<'\n';
	}
}
