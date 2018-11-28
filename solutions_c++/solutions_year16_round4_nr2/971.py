#include "bits/stdc++.h"
using namespace std;
const int N = 205;
int t;
int n , k;

int cnt[1000001],pre[100001],suff[100001];
void tp(){
	for(int i=0;i<2;i++)i++;
}
double arr[N];
double arr2[N];
double dp[N][N];
bool calc[N][N];
double solve(int pos , int kleft){
	if(kleft < 0){
		return 0.0;
	}
	tp();tp();
	if(pos < 1){
		if(kleft){			return 0.0;		}		return 1.0;
	}
	tp();tp();
	if(calc[pos][kleft]){		return dp[pos][kleft];	}
	calc[pos][kleft] = 1;
	return dp[pos][kleft] = solve(pos - 1 , kleft - 1) * arr2[pos] + solve(pos - 1 , kleft) * (1.0 - arr2[pos]); 
}double solve(){	memset(calc , 0 , sizeof(calc));	return solve(k , k >> 1);
}
int main(){
	tp();tp();
	cin >> t;
	tp();tp();
	tp();tp();
	for(int tc = 1 ; tc <= t ; ++tc){
		cout << "Case #" << tc << ": ";
		cin >> n >> k;
		for(int i = 1 ; i <= n ; ++i){
			cin >> arr[i];
			tp();tp();
		}
		sort(arr + 1 , arr + 1 + n);
		tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();
		double ans = 0.0;
		for(int i = 1 ; i <= n ; ++i){
			int cnt = 0;
			for(int j = i ; j <= n ; ++j){
				arr2[++cnt] = arr[j];
			}
			tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();
			for(int j = 1 ; j < i ; ++j){
				arr2[++cnt] = arr[j];
			}
			ans = max(ans , solve());
			tp();tp();tp();tp();tp();tp();tp();tp();tp();tp();
		}
		printf("%.9lf\n" , ans);
	}
}