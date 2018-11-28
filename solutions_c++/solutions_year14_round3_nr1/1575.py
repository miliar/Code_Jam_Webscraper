#pragma comment (linker, "/STACK:256000000")
#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;

ll mulmod(ll a, ll b, ll mod){
	if(b == 0) return 0;
	ll res = mulmod(a, b>> 1, mod);
	res += res;
	res %= mod;
	return (b & 1) ? (a + res) % mod : res;
}

int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	for(int i = 0 ; i < t ; i++){
		cout<<"Case #"<<i + 1<<": ";
		ll p, q, mod = 1ll << 40;
		scanf("%lld/%lld\n",&p,&q);
		ll exists = mulmod(p,mod,q);
		if(exists)
			cout<<"impossible"<<endl;
		else{
			vector < int > one;
			vector < int > two;
			ll elfCnt = 0;
			while(mod){
				one.push_back(mod % 10);
				mod /= 10;
			}

			while(p){
				two.push_back(p % 10);
				p /= 10;
			}

			ll ost = 0;
			vector < int > ans(one.size() + two.size(), 0);
			for(int j = 0 ; j < two.size(); j++){
				ost = 0;
				for(int z = 0; z < one.size() || ost; z++){
					int val = two[j] * (z < one.size() ? one[z] : 0) + ost;
					ost = (ans[j + z] + val);
					ans[j + z] = ost % 10;
					ost = ost / 10;
				}
			}
			while(ans.size() > 1 && ans.back() == 0)
				ans.pop_back();
			int ind = 0;
			for(int j = ans.size() - 1; j >= 0 ; j--){
				ost = ost * 10 + ans[j];
				elfCnt = elfCnt * 10 + (ost / q);
				ost %= q;
			}

			int ancector = 41;
			while(elfCnt){
				ancector --;
				elfCnt >>= 1;
			}

			cout<<ancector<<endl;
		}
	}
}