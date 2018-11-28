#include<bits/stdc++.h>
using namespace std;

int removeAhead(string& s){
	int r=0;
	if(s[s.length()-1]=='+') r=1;
	int e;
	for(e=s.length()-1; e>=0; e--){
		if(s[e]=='-'){
			break;
		}
		s[e]='-';
	}
	return r;
}

void flip(string& s){
	int i=0;
	while(i<s.length()){
		if(s[i]=='-') break;
		i++;
	}
	string ss="";
	for(int e=s.length()-1; e>=i; e--){
		char c='+';
		if(s[e]=='+') c='-';
		ss+=c;
	}
	s=ss;
}
		


int main(){
	int T;
	cin>>T;
	for(int k=1; k<=T; k++){
		cout<<"Case #"<<k<<": ";
		string s;
		cin>>s;
		
		reverse(s.begin(), s.end());
		
		int count=0;
		
		while(true){
			bool b=false;
			for(char c:s){
				if(c=='-') b=true;
			}
			if(!b) break;
			
			count+=1+removeAhead(s);
			flip(s);
		}
		cout<<count<<endl;
		
		
	}
	return 0;
}
