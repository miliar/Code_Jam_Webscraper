#include <bits/stdc++.h>

using namespace std;

#define ll				long long int
#define vi				vector<int>
#define vl				vector<ll>
#define pii				pair<int,int>
#define pil				pair<int, ll>
#define pll				pair<ll, ll>
#define pli				pair<ll, int>
#define pb				push_back
#define mp				make_pair
#define MOD				1000000007
#define F				first
#define S				second

ll pow_mod(ll a, ll b) {
	ll res = 1;
	while(b) {
		if(b & 1)
			res = (res * a);
		a = (a * a);
		b >>= 1;
	}
	return res;
}

int dflag[10];
ll maxi = -1;

ll solve(int n){

	memset(dflag,0,sizeof(dflag));

	int cnt = 0, i = 1;

	while(cnt != 10){

		int temp = i*n;

		while(temp){
			if(dflag[temp%10] == 0){
				cnt++;
				dflag[temp%10] = 1;
			}
			temp /= 10;
		}
		i++;

	}
	if(i > maxi)
		maxi = i;

	return (i-1)*n;

}

int main(){

	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;

	for(int i = 1;i<=t;i++){
		
		int n;
		cin >> n;

		cout << "Case #" << i << ": ";

		if(n == 0)
			cout << "INSOMNIA\n";
		else
			cout << solve(n) << "\n";
	}

	return 0;
}
