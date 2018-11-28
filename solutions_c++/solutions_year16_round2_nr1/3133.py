//============================================================================
// Name        : A.cpp
// Author      : Yul Obraz
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <istream>
#include <fstream>
#include <string>
#include <cstdio>
#include <vector>
using namespace std;

string calc(string t){
	char values[]={'0','2','6','4','3','1','5','7','8','9'};
	string digits[] =  {"ZERO",  "TWO", "SIX", "FOUR","THREE","ONE", "FIVE",  "SEVEN", "EIGHT", "NINE"};
	char signs[]={'Z','W', 'X','U','R', 'O','F', 'S','G','I' };
	int results[10]={0};

	int ch[256];
	for(int i=0; i<256; i++){
		ch[i]=0;
	}
	for(unsigned int i=0; t[i]!='\0'; i++){
		//cerr<< t[i];
		unsigned char uc = t[i];
		ch[uc-'A']++;
	}
	for(int i=0; i<10;i++){
		results[i]=ch[signs[i]-'A'];
		unsigned int j=0;
		while(digits[i][j]!='\0'){
			ch[digits[i][j]-'A']-=results[i];
			cerr<<(char)(digits[i][j])<<" "<<ch[digits[i][j]-'A']<<' '<<results[i]<<endl;
			j++;
		}
	}
	for(int ii=0; ii<10;ii++){
		for(int i=0; i<10;i++){
		if(values[i]==('0'+ii)){
		for(int j=0; j<results[i];j++){
			cout<<values[i];
		}
		}
		}
	}
	for(int i=0; i<256; i++){
		if(ch[i]!=0){
			cerr<<(char)('A'+i)<<" "<<ch[i]<<endl;
		}
	}
	return "x";
}
int main(int argc,char *argv[]) {
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	freopen(argv[1],"r",stdin);
	freopen(argv[2],"w",stdout);
	int tests;
	cin >> tests;
	for(int i=0; i<tests; i++){
		string target;
		cin >> target;
		cout << "Case #"<< (i+1)<<": ";
		string result = calc(target);
				cout<< endl;
	}
	return 0;
}
