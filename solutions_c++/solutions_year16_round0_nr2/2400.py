#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;cin>>t;
	for(int x=1;x<=t;x++){
		string s;cin>>s;
		char c=s[0];int l=0;
		for(int i=1;i<s.size();i++){
			if(s[i]!=s[i-1])l++;
		}
		if(s[s.size()-1]=='-')l++;
		cout<<"Case #"<<x<<": "<<l<<endl;
	}
	return 0;
}
