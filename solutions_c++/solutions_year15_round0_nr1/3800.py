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
#define name "A-large (1)"
	freopen(name ".in","r",stdin);
	freopen(name ".out","w",stdout);
	int t;
	cin>>t;
	REP(q,t){
		int smax;
		cin>>smax;
		string s;
		cin>>s;
		vector<int> inp;
		REP(i, s.size()){
			inp.PB(s[i] - '0');
		}
		int clapping = 0;
		int added = 0;
		REP(i, inp.size()){
			if(clapping < i){
				int temp = i - clapping;
				clapping += temp;
				added += temp;
			}
			clapping += inp[i];
		}
		cout<<"Case #"<<q + 1<<": "<<added<<endl;
	}
}
