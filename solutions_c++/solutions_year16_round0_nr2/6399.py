#include <iostream>
#include <string.h>
using namespace std;

int main(){
	int T,C;
	cin>>T;
	for(int t=1;t<=T;t++){
		C=0;
		string str;
		bool pl=false;
		cin>>str;
		for(int i=0;i<str.length();i++){
			char ch=str[i];
			if(ch=='-'){
				while(ch=='-'){
					i++;
					if(i>=str.length()){
						break;
					}
					ch=str[i];
				}
				C++;
				if(pl) C++;
			}
			if(ch=='+'){
				pl=true;
			}
		}
		cout<<"Case #"<<t<<": "<<C<<"\n";
	}	
	return 0;
}