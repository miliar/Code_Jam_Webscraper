#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

int main() {
	int T,i,j,k,max,NOP_UP,NOP_ADD,nc;
	
	cin>>T;
	for(nc=1 ; nc<=T ;nc++){
		cin>>max;
		//string str;
		//cin>>str;
		char str[max+1];
		cin>>str;
		NOP_UP = str[0]-'0';
		NOP_ADD = 0;
		for(i=1;i<=max;i++){
			if(i > NOP_UP && (str[i]-'0'!=0)){
				k = i - NOP_UP;
				//cout<<"inside if"<<endl;
				NOP_UP += k;
				NOP_UP += str[i]-'0';
				NOP_ADD += k;
				//cout<<NOP_ADD<<endl;
			}
			else {
				NOP_UP += str[i]-'0';
			}
		}
		cout<<"Case #"<<nc<<": "<<NOP_ADD<<endl;
	}
	return 0;
}