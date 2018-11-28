/*
 * B.cpp
 *
 *  Created on: Apr 9, 2016
 *      Author: root
 */

#include<bits/stdc++.h>
using namespace std;

#define R(Name) freopen(Name,"r",stdin);
#define W(Name) freopen(Name,"w",stdout);

bool is_good(const string &  str){
	for(int i=0;i<(int)str.size();i++){
		if(str[i] != '+')return 0;
	}
	return 1;
}


int getFirst(const string & str){
	for(int i=1;i<(int)str.size();i++){
		if(str[i] != str[i-1])
			return i;
	}
	return str.size();
}


string flip(const string & str, int len){
	string ans = "";
	for(int i=len-1;i>=0;i--){
		if(str[i] == '+')ans += '-';
		else ans += '+';
	}
	for(int i=len;i<(int)str.size();i++){
		ans += str[i];
	}
	return ans;
}



int main(){
	R("input.txt");
	W("output.txt");
	int t,ans;
	string str;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++){
		cin>>str;
		ans = 0;
		while(!is_good(str)){
			ans++;
			str = flip(str,getFirst(str));
		}
		printf("Case #%d: %d\n",cs,ans);
	}
}
