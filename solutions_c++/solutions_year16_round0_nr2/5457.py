#include<bits/stdc++.h>
using namespace std;

string invert(string str){
	string retValue=str;
	for(int i=0;i<str.length();i++)
		if(str[i]=='+')
			retValue[i]='-';
		else
			retValue[i]='+';
	return retValue;
}

int solver(string str){
	if(str.length()==0)return 0;
	int n=str.length();
	while(str[n-1]=='+'&&n>0)
		n--;
	if(n==0) return 0;
	else str=str.substr(0,n);
	while(str[n-1]=='-'&&n>0)
		n--;
	if(n==0)return 1;
	return 1 + solver(invert(str.substr(0,n)));
}

int main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		string str;cin>>str;
		cout<<"case #"<<t<<": "<<solver(str)<<endl;
	}
}