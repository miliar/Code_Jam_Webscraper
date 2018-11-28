#include <iostream>
#include <bits/stdc++.h>

using namespace::std;

int main(){
	long long int t;
	cin>>t;
	long long int k=1;
	while(t){
		t--;

		string s;
		cin>>s;
		list<char> ans;
		for(int i=0;i<s.length();i++){
			if(s[i]>=ans.front()){
				ans.push_front(s[i]);
			}else{
				ans.push_back(s[i]);
			}
		}

		cout<<"Case #"<<k<<": ";
		for(int i=0;i<s.length();i++){
			cout<<ans.front();
			ans.pop_front();
		}
		cout<<endl;
		k++;
	}
	return 0;
}
