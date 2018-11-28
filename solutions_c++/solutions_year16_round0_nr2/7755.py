#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
using namespace std;
string reverse(string temp,int start,int end){
	int i=start;
	int j=end;
	while(i<=j){
		char t=temp[i];
		temp[i]=temp[j];
		temp[j]=t;
		i++;
		j--;
	}
	i=start;
	while(i<=end){
		if(temp[i]=='+'){
			temp[i]='-';
		}
		else{
			temp[i]='+';
		}
		i++;
	}
	return temp;
}
int getValue(string str){
	int i=0;
	int j=str.size()-1;
	int count=0;
	while(str[j]=='+'){
		j--;
	}
	while(j>=0){
		i=0;
		if(str[i]=='+'){
			while(i<=j && str[i]!='-'){
				i++;
			}
			str=reverse(str,0,i-1);
			count++;
		}
		else{
			str=reverse(str,0,j);
			while(str[j]=='+'){
				j--;
			}		
			count++;
		}
	}
	return count;
}
int main(){
	int T;
	string str;
	int result;
	scanf("%d",&T);	
	for(int i=1;i<=T;i++){
		cin>>str;
		printf("Case #%d: %d\n",i,getValue(str) );
	}
	return 0;
}
