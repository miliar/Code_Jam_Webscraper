#include <iostream>
using namespace std;

int main(){
	int T;
	cin>>T;
	char str[1003];
	int need,all;
	int a;
	for(int cs=1; cs<=T; ++cs){
		cin>>a;
		cin>>str;
		need=0;
		all=0;
		for(int i=0;i<a+1;++i){
			if(all < i){
				++need;
				++all;
			}
			all+=str[i]-'0';
		}
		cout<<"Case #"<<cs<<": "<<need<<endl;
	}
	return 0;
}
