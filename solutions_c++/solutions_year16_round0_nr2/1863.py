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
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	freopen("out.txt","w",stdout);
	freopen("B-large.in","r",stdin);

	int T,C = 1;
	cin>>T;
	while(T--){
		cout<<"Case #"<<C++<<": ";
		string s;
		cin>>s;
		while(!s.empty() && s.back() == '+')
			s.pop_back();
		if(s.empty()){
			cout<<"0\n";
			continue;
		}
		int res = 2 - (s[0] == '-');
		for(int i = 1;i < s.size();i++){
			res += 2 * (s[i] == '+' && s[i-1] == '-');
		}
		cout<<res<<'\n';
	}
	return 0;
}
/**/
