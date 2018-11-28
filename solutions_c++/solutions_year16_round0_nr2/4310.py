#include <iostream>
#include <string.h>
using namespace std;

int main(){
	long long cases;
	cin>>cases;
	for(long long z=0;z<cases;z++){
		char str[101];
		cin>>str;
		long long times = 0;
		if(str[strlen(str)-1]=='-')
			times++;

		for(long long i=strlen(str)-2;i>=0;i--){
			if((str[i+1]=='+' && str[i]=='-') || (str[i+1]=='-' && str[i]=='+'))
				times++;
		}
		cout<<"Case #"<<z+1<<": "<<times<<"\n";
	}
	return 0;
}