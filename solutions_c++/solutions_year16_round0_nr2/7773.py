#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	int t;
	cin>>t;
	cin.ignore();
	for(int i=1;i<=t;i++){
		string s;
		getline(cin,s);
		int count=0;
		bool ch=false;
		if(s.size()==1 && s[0]=='-')
			count++;
		for(int j=s.size()-1;j>0;j--){
			if(s[j]=='+' && s[j-1]=='-'){
				count++;
				ch=true;
			}
			if(s[j]=='-' && !ch){
				count++;
				ch=true;
			}
			if(s[j]=='-' && s[j-1]=='+')
				count++;
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}		
	
	
			

