#include <bits/stdc++.h>
#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

int go(int pos, int comp){

}

int main(void) {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		ll k,c,s;
		cin >> k >> c >> s;
		if(k == s){
			vector<ll> ans;
			for(int i = 0; i < k; i++){
				ll aux = 0;
				ll curpot = 1;
				for(int j = 0; j < c; j++){
					aux += curpot * i;
					curpot *= k;
				}
				ans.pb(aux + 1);
			}
			cout << "Case #" << t << ":";
			for(int i = 0; i < ans.size(); i++){
				cout << " " << ans[i];
			}
			cout << endl;
		}else{

		}
	}
	
	return 0;
}
