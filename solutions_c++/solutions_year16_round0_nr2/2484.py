#include <bits/stdc++.h>
#define rep(i,n) for(int i = 0; i < n; i++)
#define INF 100000000
#define EPS 1e-10
#define MOD 1000000007
using namespace std;
typedef pair<int,int> P;

string str;

bool solve(){
	cin >> str;
	int ans = 0;
	for(int i = str.size()-1; i >= 0; i--){
		if(str[i] == '-'){
			ans++;
			for(int j = 0; j <= i; j++){
				if(str[j] == '-') str[j] = '+';
				else str[j] = '-';
			}
		}
	}
	cout << ans << endl;
}

int main(){
	int T;
	cin >> T;
	rep(i,T){
		printf("Case #%d: ",i+1);
		solve();
	}
}