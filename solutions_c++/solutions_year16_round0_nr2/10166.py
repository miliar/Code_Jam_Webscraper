#include <iostream>
using namespace std;

char flip(char a){
	if(a=='+') return '-';
	else return '+';
}



int main(){
	int T;
	cin>>T;
	for(int i = 0; i < T; i++){
		string input;
		cin>>input;
		char first = input[0];
		int count = 0;
		for(int j=1; j < input.size(); j++){
			if(first!=input[j]){
				count++;
				first = flip(first);
			}
		}
		if(first=='-') count++;
		cout<<"Case #"<<i+1<<": "<<count<<endl;	
	}
}
