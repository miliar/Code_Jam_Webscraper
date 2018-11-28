#include <iostream>

using namespace std;

int main(){
	int t,c=1;cin>>t;
	string str;
	while(c<=t){
		cin>>str;
		int p, flip=0, i = str.length()-1;
		while(i>=0){
			p = -1;
			for(;i>=0;i--){
				if(str[i]=='-' && p==-1){
					p = i;
					str[i] = '+';
				}else if(p!=-1){
					if(str[i]=='+') str[i] = '-';
					else str[i] = '+';
				}
			}
			i = p;
			if(p==-1) break;
			flip++;
		}
		cout<<"Case #"<<c++<<": "<<flip<<endl;
	}
	return 0;
}