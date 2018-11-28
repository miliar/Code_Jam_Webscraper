#include <stdio.h>
#include <iostream>
#include <string>
#include <list>

using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=1; i<=t; i++){
		cout<<"Case #"<<i<<": ";
		string str;
		cin>>str;
		list<char> lchar;
		lchar.push_back(str[0]);
		for(int j=1; j<str.length(); j++){
			if(str[j]>=*lchar.begin()){
				lchar.insert(lchar.begin(),str[j]);
			}
			else{
				lchar.push_back(str[j]);
			}
		}
		for(list<char>::iterator b=lchar.begin(); b!=lchar.end(); b++){
			cout<<*b;
		}
		cout<<endl;	
	}
}
