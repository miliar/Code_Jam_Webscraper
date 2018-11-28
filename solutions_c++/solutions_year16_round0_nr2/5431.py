#include <iostream>
#include <string>
using namespace std;

int foo(string &s){
	int l = s.size();
	char crt = s[0];
	if(l==1)return crt=='-'?1:0;
	int count = 0;
	for(int i=0;i<l-1;i++){
		if(s[i]!=s[i+1])count++;
	}
	return s[l-1]=='+'?count:count+1;
}
int main(){
	int T;
	cin>>T;
	int x=0;
	string s;
	while(T--){
		cin>>s;
		x++;
		cout << "Case #"<<x<<": "<<foo(s)<<endl;
	}
	return 0;
}
