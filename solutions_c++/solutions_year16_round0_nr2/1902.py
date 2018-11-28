#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <stack>
#include <iostream>

using namespace std;

int minflips(string &str){
	int ret=0;
	for(int i=str.length()-1; i>=0; i--){
		if(str[i]=='-'){
			if(str[0]=='-'){
				string tmp="";
				for(int j=0; j<=i; j++){
					if(str[j]=='+') tmp='-'+tmp;
					else tmp='+'+tmp;
				}
				for(int j=0; j<=i; j++) str[j]=tmp[j];
				ret++;
			}
			else{
				// find longest '+' string
				// flip that
				for(int j=0; j<i; j++){
					if(str[j]=='+') str[j]='-';
					else break;
				}
				// then flip i-0
				string tmp="";
				for(int j=0; j<=i; j++){
					if(str[j]=='+') tmp='-'+tmp;
					else tmp='+'+tmp;
				}
				for(int j=0; j<=i; j++) str[j]=tmp[j];
				ret+=2;
			}
		}
	}
	return ret;
}

int main(){
	int t;
	scanf("%d",&t);
	for(int i=1; i<=t; i++){
		printf("Case #%d: ",i);
		string str;
		cin>>str;
		int mf=minflips(str);
		printf("%d\n",mf);
	}
}
