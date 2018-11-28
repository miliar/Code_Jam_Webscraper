#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long
#define endl "\n"
#define mp make_pair
#define pb push_back
ll arr[110];
int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t,k,c,s;
	cin >> t;
	int cnt=1;
	while(t--){
		cin >> k >> c >> s;
		rep(i,k) arr[i]=i;
		rep(i,c-1){
			rep(j,k){
				arr[j]*=k;
			}
		}
		if(k == s){
			cout << "Case #" << cnt++ << ": ";
			rep(i,k){
				cout << arr[i]+1 << " ";
			}
			cout << endl;

		}
		else{
			cout << "Case #" << cnt++ << ": " << "IMPOSSIBLE" << endl;

		}

		
	}
	return 0;
}