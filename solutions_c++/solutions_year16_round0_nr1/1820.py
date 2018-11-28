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
	freopen("A-large.in","r",stdin);
	int T,C = 1;
	cin>>T;
	long long N;
	while(T--){
		cout<<"Case #"<<C++<<": ";
		cin>>N;
		if(N == 0){
			cout<<"INSOMNIA\n";
			continue;
		}
		long long cur = 1;
		set<int> cnt;
		for(int i = 0;i < 10;i++)cnt.insert(i);
		while(!cnt.empty()){
			auto t = cur * N;
			while(t){
				cnt.erase(t%10);
				t /= 10;
			}
			cur++;
		}
		cout<<(cur-1) * N<<'\n';
	}
	return 0;
}
/**/
