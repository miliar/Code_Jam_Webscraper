#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;
bool check(string s){
	for(int i=0;i<s.length();i++){
		if(s[i]!='+') return false;
	}
	return true;
}
string func(int i,string s){
	for(int j=0;j<=i;j++){
		if(s[j]=='-') s[j]='+';
		else s[j]='-';
	}
	return s;
}
int main() {
	int t;
	cin>>t;
	int k=0;
	while(t--){
		k++;
		string s;
		cin>>s;
		int n=0;
		int p=s.length()-1;
		for(int i=p;i>=0;i--){
 
			if(check(s)) break;
			if(s[i]=='-'){
				s=func(i,s);
				n++;
			}
		}
		cout<<"Case #"<<k<<": "<<n<<endl;
	}
}