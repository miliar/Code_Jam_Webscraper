#include <iostream>

using namespace std;

int testcase = 0;

void solve(){
	testcase++;
	string s;
	cin>>s;
	int ans = 0;
	int len = s.size();
	int i = len-1;
	char c = '-';
	while(i>=0){
		if(s[i]==c){
			ans++;
			if(c=='-') c = '+';
			else c = '-';
		}
		i--;
	}
	cout<<"Case #"<<testcase<<": "<<ans<<endl;
}

int main(){
	int t;
	cin>>t;
	while(t--) solve();
	return 0;
}