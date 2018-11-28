/*input
5
4 11111
1 09
5 110011
10 91000000001
0 1
*/
#include <bits/stdc++.h>
#define X first
#define Y second
using namespace std;
void solve(){
	int smax;
	cin>>smax;
	string s;
	cin>>s;
	int n=s.length();
	long long curr=0;
	long long ans=0;
	for (int i = 0; i < n; i++){
		if(curr<(long long)i && s[i]!='0'){
			ans+=(long long)(i-curr);
			curr+=(i-curr);			
		}
		curr+=(long long)(s[i]-'0');
	}	
	cout<<ans<<endl;
}
int main(){
	ios_base::sync_with_stdio(false);
	freopen("C:/Users/Enjoy/Desktop/input.txt","r",stdin);
	freopen("C:/Users/Enjoy/Desktop/output.txt","w",stdout);
	int t;cin>>t;
	int xx=1;
	while(t--){
		cout<<"Case #"<<xx++<<": ";
		solve();
	}
	return 0;
}