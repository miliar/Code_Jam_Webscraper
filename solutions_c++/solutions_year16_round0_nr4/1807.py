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
long long pwr(long long base,long long power){
	long long res = 1;
	while(power){
		if(power&1)res *= base;
		base *= base;
		power >>= 1;
	}
	return res;
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("out.txt","w",stdout);
	freopen("D-small-attempt0.in","r",stdin);

	int T,c = 1;
	long long K,C,S;
	cin>>T;
	while(T--){
		cout<<"Case #"<<c++<<": ";
		cin>>K>>C>>S;
		long long cur = 1,en = pwr(K,C),ad = en / K;
		while(cur <= en){
			cout<<cur<<" \n"[cur + ad > en];
			cur += ad;
		}
	}
	return 0;
}
/**/
