#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

void func(int table[26], vector<int>& num){
	while(table['Z'-'A']>0){
		num.push_back(0);
		table['Z'-'A']--;
		table['E'-'A']--;
		table['R'-'A']--;
		table['O'-'A']--;
	}
	while(table['W'-'A']>0){
		num.push_back(2);
		table['T'-'A']--;
		table['W'-'A']--;
		table['O'-'A']--;
	}
	while(table['U'-'A']>0){
		num.push_back(4);
		table['F'-'A']--;
		table['O'-'A']--;
		table['U'-'A']--;
		table['R'-'A']--;
	}
	while(table['X'-'A']>0){
		num.push_back(6);
		table['S'-'A']--;
		table['I'-'A']--;
		table['X'-'A']--;
	}
	while(table['G'-'A']>0){
		num.push_back(8);
		table['E'-'A']--;
		table['I'-'A']--;
		table['G'-'A']--;
		table['H'-'A']--;
		table['T'-'A']--;
	}
	while(table['O'-'A']>0){
		num.push_back(1);
		table['O'-'A']--;
		table['N'-'A']--;
		table['E'-'A']--;
	}
	while(table['T'-'A']>0){
		num.push_back(3);
		table['T'-'A']--;
		table['H'-'A']--;
		table['R'-'A']--;
		table['E'-'A']-=2;
	}
	while(table['F'-'A']>0){
		num.push_back(5);
		table['F'-'A']--;
		table['I'-'A']--;
		table['V'-'A']--;
		table['E'-'A']-=2;
	}
	while(table['S'-'A']>0){
		num.push_back(7);
		table['S'-'A']--;
		table['E'-'A']-=2;
		table['V'-'A']--;
		table['N'-'A']--;
	}
	while(table['I'-'A']>0){
		num.push_back(9);
		table['N'-'A']-=2;
		table['I'-'A']--;
		table['E'-'A']--;
	}
}


int main(){
	ofstream myfile;
  	myfile.open ("outputa.txt");
  	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;++i){
		string s;
		cin>>s;
		int len=s.length();
		int table[26]={0};
		for (int i=0;i<len;++i){
			table[s[i]-'A']++;
		}
		vector<int> res;
		func(table,res);
		sort(res.begin(),res.end());
		myfile<<"Case #"<<i<<": ";
		for (int a:res) myfile<<a;
		myfile<<endl;
	}
  	myfile.close();
  	return 0;
}
