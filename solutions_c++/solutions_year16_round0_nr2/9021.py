#include<iostream>
#include<string>
#include<fstream>
using namespace std;

string S;

bool compare(){

	for(int i=0;i<S.length();i++){
		if(S.at(i)==('-'))
			return false;
	}
	return true;
}


void flip(){
		
	int tt = S.find('-');
	int pp = S.find('+');
	string temp=S;

	if(pp<0 || pp>100000){
		for(int i=0;i<S.length();i++){
			temp.at(i)='+';
		}
	}else if(tt==S.rfind('-') && tt==0){
		temp.at(0)='+';
		
	}else if(tt>0){
		for(int i=0;i<tt;i++){
			temp.at(i)='-';
		}
	}
	else if(pp>0 && pp<100){
		for(int i=0;i<pp;i++){
			temp.at(i)='+';
		}
	}else if(tt==0){
		if((S.at(S.length()-1)) == '-'){
			for(int i=0;i<S.length();i++){
				if(S.at(S.length()-i-1)=='-' ){
					temp.at(i)='+';
				} 	
				else {
					temp.at(i)='-';
				}
			}	
		}
		else{	
			for(int i=0;i<tt;i++){
				if(S.at(tt-i)==('-')){
					temp.at(i)='+';
				} 	
				else {
					temp.at(i)='-';
				}
			}
		}
	}
	S=temp;
}

bool check(string atr){
	for(int abc=0;abc<atr.length();abc++){
		if(atr.at(abc)!='+'){
			if(atr.at(abc)!='-'){
				return false;
			}
			else
				return true;	
		}
	}
	return true;
}
main() {
	int T,count=1;
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	fin >> T;
	while(T>=1 && T<=100){
		
		int N=0;
		fin >> S;

		if(S.length()>0 && S.length()<=100){
			if(check(S)){
				while(!compare()){
				N++;
				flip();		
				}
				fout << "Case #"<<count<<": " << N << endl;	
			}
		}
		T--;
		count++;
	}
}
