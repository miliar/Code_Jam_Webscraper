#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int main(){
	int t,shy_max;
	string s;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		cin>>shy_max>>s;
		int extra = 0;
		int number_stood=0;
		for(int j=0;j<s.length();j++){
			int temp = s[j]-48;
			if(number_stood>=j || temp==0){
				//cout<<number_stood<<endl;
				number_stood+=temp;
				//cout<<number_stood<<endl<<endl;
			}
			else if(number_stood<j){
				//cout<<j<<" "<<number_stood<<endl;
				//cout<<extra<<" "<<j-number_stood<<endl;
				extra+=(j-number_stood);
				number_stood+=extra;
				number_stood+=temp;
			}
		}
		cout<<"Case #"<<i+1<<": "<<extra<<endl;
	}
}