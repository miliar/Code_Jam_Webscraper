#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
	int t,temp=1;
	cin>>t;
	while(temp!=t+1){
		string s;
		cin>>s;
		cout<<"Case #"<<temp<<": ";
		temp++;
		
		ll answer = 1;
		char prev=s[0];
		char minus='-';
		for(ll i=0;i<s.length();i++){
			if(s[i]!=prev){
				answer++;
				prev = s[i];
			}
		}
		if(prev==minus)
			cout<<answer<<endl;
		else
			cout<<answer-1<<endl;
	}
	return 0;
}
