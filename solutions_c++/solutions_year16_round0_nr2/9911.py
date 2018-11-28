#include <iostream>
#include <string>
using namespace std;
int main(){
	int T,i,count;
	string s;
	cin>>T;
	i=T;
	while(T>0){
		count = 0;
		cin>>s;
		for(int j=0;j<s.size();j++){
			if(s[j]=='-') count=count+2;
			while(s[j]=='-'){
				j++;
			}
		}
		if(s[0]=='-') count--;
		T--;
		cout<<"Case #"<<i-T<<": "<<count<<"\n";
	}
	return 0;
}