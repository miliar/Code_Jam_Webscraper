#include <iostream>
#include <string>

using namespace std;

int main(){
	int n;
	string str;
	char prev='+';
	int change;

	cin>>n;
	for(int j=0;j<n;j++){
		cin>>str;

		if(str.length()==1 && str[0]=='+'){
			cout<<"Case #"<<(j+1)<<": "<<"0"<<endl;
		}else if(str.length()==1 && str[0]=='-'){
			cout<<"Case #"<<(j+1)<<": "<<"1"<<endl;
		}else{
			change=0;
			prev='+';

			for(int i=str.length()-1;i>=0;i--){
				if(str[i]!=prev){
					change++;
					prev=str[i];
				}
			}

			cout<<"Case #"<<(j+1)<<": "<<change<<endl;
		}
	}
}