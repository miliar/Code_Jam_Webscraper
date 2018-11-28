#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

int func(string s){
	int count=0;
	int i=0,n=s.length();
	while(i<n){
		count++;
		int j=i+1;
		while(j<n&&s[j]==s[i]) j++;
		i=j;
	}
	if (s[n-1]=='+') count--;
	return count;
}

int main(){
	ofstream myfile;
  	myfile.open ("outputb.txt");
	int t;
	cin>>t;
	for (int i=1;i<=t;++i){
		string s;
		cin>>s;
		myfile<<"Case #"<<i<<": "<<func(s)<<endl;
	}
	myfile.close();
}
