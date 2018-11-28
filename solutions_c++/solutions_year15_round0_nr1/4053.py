//A
#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

int main(){
	int t;
	cin>>t;
	int n = t;
	while(t--){
		int s;
		cin>>s;
		cin.ignore();
		string  str;
		cin>>str;
		int r=0;
		int pes=0;
		for(int i=0;i<s+1;i++){
			if(pes>=i){
				pes+=str[i]-'0';
			}else{
				r+=abs(pes-i);
				pes+=(str[i]-'0')+abs(pes-i);
			}
		}
		cout<<"Case #"<<n-t<<": "<<r<<endl;
	}
}
