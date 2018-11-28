#include<iostream>
#include<string>
#include<algorithm>
#define forn(i, n) for(int i=0; i<n; i++)
using namespace std;

int solve(string s){
	int ans = 0, no = (s[0]-'0');
	forn(i, s.length()){
		if(i==0)continue;
		//cout<<i<<" "<<no<<" "<<ans<<" "<<i-no<<endl;
		if(no<i)ans += i-no, no = i + (s[i]-'0');
		else no += (s[i]-'0');
	}
	return ans;
}

int main(){
	int t, a;
	string s;
	cin>>t;
	forn(i, t){
		cin>>a>>s;
		cout<<"Case #"<<i+1<<": "<<solve(s)<<endl;
	}
	return 0;
}

