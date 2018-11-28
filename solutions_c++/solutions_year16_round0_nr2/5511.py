#include<iostream>
#include<cstring>

using namespace std;


int main(){
	int t;
	cin>>t;
	for(int l=1;l<=t;l++){
		string s;
		cin>>s;
		int ans=0;
		for(int i=0;i<s.size();i++){
			if(i==0 && s[i]=='-')ans++;
			if(i>0 && s[i]=='-' && s[i-1]=='+')ans+=2;
		}
		cout<<"Case #"<<l<<": "<<ans<<endl;
	}
	return 0;
}
