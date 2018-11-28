#include <bits/stdc++.h>
using namespace std;
const int dx[]={1,0,-1,0,1,-1,-1,1};
const int dy[]={0,1,0,-1,1,1,-1,-1};
const int INF = 1<<30;
const long long LINF = 1e18;
const int EPS = 1e-8;
#define PB push_back
#define mk make_pair
#define fr first
#define sc second
#define ll long long
#define reps(i,j,k) for(int i = (j); i < (k); i++)
#define rep(i,j) reps(i,0,j)
#define MOD 1000000007
typedef pair<int,int> Pii;
typedef pair<int, ll> Pil;
typedef vector<int> vi;
typedef vector<vi> vvi;
bool check(bool memo[20]){
	rep(i,10){
		if(memo[i] == false){
			return false;
		}
	}
	return true;
}
ll solve(int _N){
	bool memo[20]={false};
	int cnt = 0;
	ll N = (ll)_N;
	do{
		cnt++;
		N*=cnt;
		ll c = N;
		memo[c%10]++;
		while(c/10!=0){
			memo[c%10]++;
			c/=10;
		}
		memo[c%10]++;
		N = (ll)_N;
	}while(!check(memo) && cnt<=200000);
	if(check(memo) == false){
		return -1;
	}
	return N*cnt;
}
int main(){
	int Q;
	cin >> Q;
	rep(q,Q){
		int N;
		scanf("%d",&N);
		ll res = solve(N);
		if(res == -1){
			printf("Case #%d: INSOMNIA\n",q+1);
		}
		else{
			printf("Case #%d: %lld\n",q+1,res);
		}
	}
	return 0;
}