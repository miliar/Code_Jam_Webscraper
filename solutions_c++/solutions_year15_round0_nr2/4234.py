using namespace std;
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cassert>
#include<cstring>
#include<cmath>
#include<set>
#include<map>
#include<fstream>
#include<sstream>
typedef long double D; typedef long long LL; typedef pair<int,int> pii;
#define ALL(v) (v).begin(),(v).end()
#define REP(i, n) for (int i (0); i < (n); i ++)
#define FORIT(a,b, it) for(__typeof(b)it(a);it!=(b);++it)
#define FOREACH(v, it) FORIT((v).begin(),(v).end(),it)
#define len(v) ((int)(v).size())
#define append push_back
#define _ make_pair
#define fi first
#define se second
#define add insert
#define remove erase
#define TWO(x) (1<<(x))
#define UNIQUE(v) (v).erase(unique(ALL(v)),(v).end())
const int infInt (1010101010);
const LL  infLL  (4 * LL (infInt) * LL (infInt));
int dp[1005][1005];//N,K -> min #stappen om blok van lengte N in stukken van lengte <=K te verdelen.
int main(){
	for(int n=1;n<=1000;n++){
		for(int k=1;k<=1000;k++){
			if(k>=n)dp[n][k]=0;else{
				dp[n][k]=1e9;
				for(int p=1;p<n;p++)dp[n][k]=min(dp[n][k],1+dp[p][k]+dp[n-p][k]);
			}
		}
	}
	int T; cin >> T;
	for(int it=1;it<=T;it++){
		int N;cin>>N;
		vector<int>v(N);REP(i,N)cin>>v[i];
		int ans=1e9;
		for(int re=1;re<=1000;re++){
			int s=0;REP(i,N)s+=dp[v[i]][re];
			ans=min(ans,re+s);
		}
		cout<<"Case #"<<it<<": "<<ans<<endl;
	}
}
