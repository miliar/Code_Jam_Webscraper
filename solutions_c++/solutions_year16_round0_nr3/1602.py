/**/
#include<bits/stdc++.h>
using namespace std;
/***********************************************/
/*      ____________
 *     /            \
 *    /  /\      /\  \
 *   /  /  \    /  \  \
 *   \                /
 *    \     \___/    /
 *     \____________/
 */
const long long mod = 1000000007;
long long pow_mod(long long base,long long power,long long md){
	long long res = 1;
	while(power){
		if(power&1)res = (res * base)%md;
		base = base * base % md;
		power >>= 1;
	}
	return res;
}
vector<long long> p = {2,3,5,7,11,13,17,19,23,29,31,839,1129,5441,58427};
long long prime(long long x,long long base){
	long long t = x;
	for(auto pi : p){
		x = t;
		long long cur = 0;
		int i = 0;
		while(x){
			if(x&1){
				cur = (cur + pow_mod(base,i,pi))%pi;
			}
			i++;
			x >>= 1;
		}
		if(cur == 0)return pi;
	}
	return -1;
}
string bin(long long x){
	string res = "";
	while(x){
		res += (x&1?'1':'0');
		x >>= 1;
	}
	reverse(res.begin(),res.end());
	return res;
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("out.txt","w",stdout);
	freopen("C-large.in","r",stdin);

	cout<<"Case #1:\n";
	vector<pair<long long,vector<long long> > > to;
	for(long long i = 0;i < (1ll<<29);i++){
		long long cur = i*2ll + 1ll + (1ll<<31);
		vector<long long> ad;
		for(int i = 2;i <= 10;i++)ad.push_back(prime(cur,i));
		if(find(ad.begin(),ad.end(),-1) == ad.end()){
			to.push_back({cur,ad});
			if(to.size() >= 500)break;
			cerr<<cur<<endl;
		}
	}
	for(auto x : to){
		cout<<bin(x.first)<<' ';
		for(int i = 2;i <= 10;i++)
			cout<<x.second[i-2]<<" \n"[i == 10];
	}
	return 0;
}
/**/
