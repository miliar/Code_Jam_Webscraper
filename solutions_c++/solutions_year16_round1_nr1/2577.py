#include <bits/stdc++.h>

using namespace std;

int main(){
	int t;
	string s;
	deque<char> ans;
	int cont=1;
	cin>>t;
	while(t--){
		cout<<"Case #"<<cont<<": ";
		cont++;
		cin>>s;
		ans.clear();
		ans.push_back(s[0]);
		for(int i=1;i<s.size();i++){
			if(s[i]>=ans.front())
				ans.push_front(s[i]);
			else
				ans.push_back(s[i]);
		}
		for(int i=0;i<s.size();i++)
			cout<<ans[i];
		cout<<"\n";
	}
	return 0;
}