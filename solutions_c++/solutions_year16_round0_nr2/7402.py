#include<iostream>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i = 1; i <=t; i++){
		string s;
		cin>>s;
		int count = 0;
		for(int j = s.size()-1; j >= 0; j--){
			if(s[j] == '-'){
				count++;
				for(int k = j; k >= 0; k--){
					if(s[k] == '-'){
						s[k] = '+';
					}
					else{
						s[k] = '-';
					}
				}
			}
		}
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
