#include <bits/stdc++.h>
using namespace std;
int x[55];
int main(){
	int t,i,j;string s;
	cin>>t;
	for(i=1;i<=t;++i){
		cout<<"Case #"<<i<<": ";
		cin>>s;
		int pos=0;
		string t;
		for(j=0;j<s.size();++j){
			if(j!=0){
				if(s[j]==s[j-1])continue;
			}
			t+=s[j];
		}
		int ret=0,c=0;
		for(j=0;j<t.size();++j){
			if(t[j]=='-'){
				if(j!=0 && t[j-1]=='+')ret+=2;
				else
					++ret;
			}
		}
		cout<<ret<<endl;
	}
}
