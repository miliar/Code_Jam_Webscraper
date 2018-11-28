#include <bits/stdc++.h>
#define int long long
#define ll long long

using namespace std;
main (){
	ios::sync_with_stdio(0);
	cin.tie(0);
	int z = 1;
	for (int u = 0; u < z; ++u){
		ll N= 32;
	//	cin >> N >> J;
		
		cout <<"Case #" << u+1 << ": \n";
			for (int i = 3; i < 1002; i += 2){
				int s = 0;
				for (int x =0; x < 10; ++x){
					if (i & (1<<x))s = x;
				}
				++s;
				int k = i;
				while (k){
					if (k&1)cout <<"1";
					else cout <<"0";
					k >>= 1;
				}
				for (int j = 1; j <= N - 2*s;++j)cout <<"0";
				k = i;
				while (k){
					if (k&1)cout <<"1";
					else cout <<"0";
					k >>= 1;
				}
				cout << ' ';
				for (int j =2; j <= 10; ++j){
					ll d = 0;
					vector <int> pot(s);
					pot[0] = 1;
					for (int x = 1; x < s; ++x){
						pot[x] = j*pot[x-1];
					}
					for (int x =0; x < s; ++x){
						if (i & (1<<x))d += pot[s-x-1];
					}
					cout << d << ' ';
				}
				cout << '\n';
			}
			
		
	}
}
