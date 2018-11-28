#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long long ll;
typedef vector<bool> vb;

vector<pair<int, vi> > ans;

int main(void) {
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		int N, J;
		cin >> N >> J;
		ans.clear();	

		ll cur = 1;
		int tot = 0;
		while(tot < J) {
			vi divs;
			bool okok = true;
			for(int i = 2; i <= 10; i++){
				ll aux = cur;
				ll num = 0;
				ll p = 1;
				while(aux){
					num += (aux%2)*p;
					p*=i;
					aux/=2;
				}
				bool ok = false;
				for(int j = 2; j <= 10000; j++){
					ll lastdmod = 1;
					for(int k = 0; k < N - 1; k++){
						lastdmod = (lastdmod*i)%j;
					}

					if((lastdmod + num)%j == 0){
						ok = true;
						divs.pb(j);
						break;
					}
				}

				if(!ok){
					okok = false;
					break;
				}
			}

			if(okok){
				tot++;
				ans.pb(mp(cur, divs));
			}
			cur += 2;
		}
		cout << "Case #" << t << ":" << endl;
		for(int i = 0; i < ans.size(); i++){
			vi b;
			ll aux = ans[i].fi;
			int cnt = 0;
			while(aux){
				b.pb(aux%2);
				cnt++;
				aux/=2;
			}

			for(int j = 0; j < N-cnt-1; j++){
				b.pb(0);
			}
			b.pb(1);
			reverse(b.begin(), b.end());
			for(int j = 0; j < b.size(); j++){
				cout << b[j];
			}

			for(int j = 0; j < ans[i].se.size(); j++){
				cout << " " << ans[i].se[j];
			}
			cout << endl;
		}
	}
	return 0;
}
