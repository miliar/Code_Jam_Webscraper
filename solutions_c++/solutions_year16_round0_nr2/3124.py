#include "math.h"
#include "iostream"
#include "fstream"
#include "vector"
#include "string"
#include "set"
#include "unordered_set"
#include "stack"
using namespace std;

bool checks( vector <bool> v){
	for(int i=0;i<v.size();i++){
		if(v[i]==0){
			return 0;
		}
	}
	return 1;
}

void flippan( vector <bool> & pancake){
	int i=0;
	pancake[i]=!pancake[i];
	while(pancake[i]!=pancake[i+1]){
		i=i+1;
		pancake[i]=!pancake[i];
	}
}

int main(){
	int T;
	ifstream in("inputl.txt");
	ofstream out("output.txt");
	in>>T;
	for(int i=0;i<T;i++){
		vector <bool> pancake;
		string panin;
		in>>panin;
		for(int k=0;k<panin.size();k++){
			if(panin[k]=='+'){
				pancake.push_back(1);
			}
			else pancake.push_back(0);
		}
		int ct=0;
		while(checks(pancake)==0){
			ct++;
			flippan(pancake);
		}
		out<<"Case #"<<i+1<<": "<<ct<<endl;
	}
}
