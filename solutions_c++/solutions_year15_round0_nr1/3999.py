#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int j=1;j<=t;j++) {
		int smax;
		string vector;
		cin>>smax;
		cin>>vector;
		int standing=0,friends=0;
		for(int i=0;i<=smax;i++) { 
			if(vector[i]-'0'){
				if (standing<i){
				friends+=i-standing;
				standing+=i-standing;
				}
				standing+=vector[i]-'0';
		}}
		cout<<"Case #"<<j<<": "<<friends<<endl;
	}
	return 0;
}

