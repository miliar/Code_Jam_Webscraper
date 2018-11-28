#include <bits/stdc++.h>
 
using namespace std;
 
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))
 
#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second
typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;
int dp[1000009];

int main(){
	int ite;
	dp[1]=1;
	for(int i=1;i<1000001;i++){
		int ans = dp[i]+1;
		if(dp[i+1]==0 || dp[i+1]>ans) dp[i+1] = dp[i]+1;
		int q=0, q1=i;
		while(q1){
			q*=10;
			q+= q1%10;
			q1/=10;
		}	
		if(q>1000000) continue;
		if((dp[q]==0)||(dp[q]>ans) ){
			// cout<<i<<' '<<q<<endl;
			// getchar();
			dp[q] = ans;
		}
	}

	cin>>ite;
	int o=1;
	while(ite--){
		cout<<"Case #"<<o++<<": ";
		int n;
		cin>>n;
		cout<<dp[n]<<endl;
	}
}