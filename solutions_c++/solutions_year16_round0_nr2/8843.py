#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

int main(){
	int T,times;
	char plus='+',minus='-',sign;
	string str;	
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		str.clear();
		cin>>str;
		times = 0;
		sign=' ';
		for(int j=0;j<str.size()-1;j++){
			if(str[j] != str[j+1]){
				sign =(str[j]=='+') ? minus:plus;
					str[0]=sign;	
				times++;
			}
		}
		if(str[0]=='-')
			times++;
		printf("Case #%d: %d\n",i,times);
	
	
	}


	return 0;
}
