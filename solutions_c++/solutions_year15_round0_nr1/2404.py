#include <iostream>
#include <algorithm>
using namespace std;
string s;
int n;
long long solve(){
	long long par=0LL;
	long long ans=0LL;
	if(s[0]>='0')par+=(s[0]-'0');
	for(int i=1;i<(int)s.size();i++){
		if(s[i]=='0')continue;
		if(i<=par){
			par+=(s[i]-'0');
		}
		else{
			ans+=(i-par);
			par+=(i-par);
			par+=(s[i]-'0');
		}
	}
	return ans;
}
int main(){
	//ios::sync_with_stdio(false);
	//cin.tie(0);
	int cases;
	cin>>cases;
	int tc=1;
	while(cases--){
		cin>>n>>s;
		cout<<"Case #"<<tc++<<": "<<solve()<<"\n";
	}
	return 0;
}
