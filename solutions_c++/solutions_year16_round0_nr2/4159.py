#include <iostream>
#include <vector>

using namespace std;

int inve(string s){
	int ret = 1;
	for(int i = 1; i < s.length(); i++){
		if(s[i] != s[ i - 1]) ret ++;
	}
	return ret;
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, n, i, j;
	string s;
	cin>>t;
	for(i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		cin>>s;
		for(j = 0; j < s.length(); j++){
			if(s[j] == '-') break;
		}
		if(j == s.length()) cout<<0<<endl;
		else{
			int ans = inve(s);
			if(s[s.length() - 1] == '+') ans--;
			cout<<ans<<endl;
		}
	}
}
