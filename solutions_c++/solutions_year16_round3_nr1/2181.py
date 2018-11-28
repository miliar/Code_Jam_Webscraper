#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
#define PB push_back
#define ALL(a)  (a).begin(),(a).end()
#define SZ(a) int((a).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define RFOR(i,a,b) for (int i=(b)-1;i>=(a);i--)
#define REP(i,n)  FOR(i,0,n)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)
#define RBP(i,a) for(auto& i : a)
#ifdef LOCAL111
	#define DEBUG(x) cout<<#x<<": "<<(x)<<endl
#else
	#define DEBUG(x)
#endif
#define F first
#define S second
#define SNP string::npos
#define WRC(hoge) cout << "Case #" << (hoge)+1 << ": "
#define INF 1e8

typedef pair<int,int> P;
typedef long long int LL;
typedef unsigned long long ULL;
typedef pair<LL,LL> LP;

void ios_init(){
#ifdef LOCAL111
	return;
#endif
	ios::sync_with_stdio(false); cin.tie(0);	
	//cout.setf(ios::fixed);
	//cout.precision(12);
}

int main()
{
	ios_init();
	int T;
	cin >> T;
	REP(hoge,T){
		int n;
		cin >> n;
		vector<int> p(n);
		//int sum = 0;
		REP(i,n) cin >> p[i];
		priority_queue<P> qu;
		/*REP(i,n){
			//if(p[i] != 0) qu.push(P(p[i],i));
			sum += p[i];
		}*/
		vector<string> ans;
		while(true){
			priority_queue<P> qu;
			REP(j,n){
				if(p[j] >= 2){
					qu.push(P(p[j],j));
				}
			}
			if(qu.empty()) break;
			string s;
			auto t1 = qu.top();
			qu.pop();
			p[t1.S]--;
			s += 'A'+t1.S;
			if(!qu.empty()){
				auto t2 = qu.top();
				qu.pop();
				p[t2.S]--;
				s += 'A'+t2.S;
			}
			ans.push_back(s);
		}
		if(n&1){
			string s;
			ans.push_back("A");
			for(int i = 1;i < n-1; i += 2){
				string s;
				s += 'A'+i;
				s += 'A'+i+1;
				ans.push_back(s);
			}
		}else{
			for(int i = 0;i < n-1; i += 2){
				string s;
				s += 'A'+i;
				s += 'A'+i+1;
				ans.push_back(s);
			}
		}
		/*while(!qu.empty()){
			string s;
			P t1(-1,-1),t2(-1,-1);
			t1 = qu.top();
			qu.pop();
			if(!qu.empty()){
				t2 = qu.top();
				qu.pop();
			}
			if(t2 != P(-1,-1)){
				if(t1.F != t2.F){
					s += 'A'+t1.S;
					if(t1.F-1 != 0)	qu.push(P(t1.F-1,t1.S));
					qu.push(t2);
				}else{
					DEBUG(t1.S);
					DEBUG(t1.F);
					s += 'A'+t1.S;
					s += 'A'+t2.S;
					if(t1.F-1 != 0) qu.push(P(t1.F-1,t1.S));
					if(t2.F-1 != 0) qu.push(P(t2.F-1,t2.S));
				}
			}else{
				assert(false);
			}
			ans.push_back(s);
		}*/
		WRC(hoge);
		REP(i,SZ(ans)) cout << ans[i] << (i != SZ(ans)-1?' ':endl);
	}
	return 0;
}
