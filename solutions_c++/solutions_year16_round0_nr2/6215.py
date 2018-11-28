#include <bits/stdc++.h>
using namespace std;
string toString(long long int asd){
	stringstream ss;
	ss<<asd;
	return ss.str();
}
int main(){
	freopen ("B-large.in","r",stdin);
	freopen ("B-large.out","w",stdout);
	int t;
	string s;
	cin>>t;
	for(int tc = 1; tc <= t; tc++){
		cin>>s;
		int cnt = 1;
		cout<<"Case #"<<tc<<": ";
		for(int i = 1; i < s.size();i++){
			if(s[i] != s[i-1])cnt++;
		}
		if(s[s.size()-1] == '+')cout<<cnt - 1<<endl;
		else cout<<cnt<<endl;
	}
	return 0;
}