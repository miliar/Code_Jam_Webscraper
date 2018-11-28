#include<iostream>
#include<string>
using namespace std;

void solve(int t){
	string S;
	cin>>S;
	int n=S.size(),j=0,x=1;
	char s[100];
	for(string::iterator i=S.begin();i!=S.end();++i){
		s[j]=*i;
		++j;
	}
	for(j=1;j<n;++j){
		if(s[j]!=s[j-1]){
			++x;
		}
	}
	cout<<"Case #"<<t<<": ";
	if(s[n-1]=='-'){
		cout<<x<<endl;
	}else{
		cout<<x-1<<endl;
	}
}

int main(){
	int T;
	cin>>T;
	for(int t=1;t<=T;++t){
		solve(t);
	}
}