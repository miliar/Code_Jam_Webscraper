#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int t,a;
	cin>>t;
	for(a=1;a<=t;a++){
		char s[100];
		cin>>s;
		int i,count=0;
		for(i=0;i<strlen(s)-1;i++){
		if(s[i]=='-'&&s[i+1]=='+')
		count++;
		else if(s[i]=='+'&&s[i+1]=='-')
		count++;
		}
		if(s[i]=='-')
		count++;
		cout<<"Case #"<<a<<": "<<count<<endl;
	}
	return 0;
}