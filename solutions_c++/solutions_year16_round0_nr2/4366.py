#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <bits/stdc++.h>
using namespace std;


#define cout fout
#define cin fin


//string print(char ch){
//	switch(ch){
//		case 'a':return("2");
//		case 'b':return("22");
//		case 'c':return("222");
//		case 'd':return("3");
//		case 'e':return("33");
//		case 'f':return("333");
//		case 'g':return("4");
//		case 'h':return("44");
//		case 'i':return("444");
//		case 'j':return("5");
//		case 'k':return("55");
//		case 'l':return("555");
//		case 'm':return("6");
//		case 'n':return("66");
//		case 'o':return("666");
//		case 'p':return("7");
//		case 'q':return("77");
//		case 'r':return("777");
//		case 's':return("7777");
//		case 't':return("8");
//		case 'u':return("88");
//		case 'v':return("888");
//		case 'w':return("9");
//		case 'x':return("99");
//		case 'y':return("999");
//		case 'z':return("9999");
//		case ' ':return("0");
//
//
//	}
//}

int main() {
    //Enter your code here. Read input from STDIN. Print output to STDOUT
	ofstream fout("C:\\Users\\Harry\\Desktop\\temp");
	ifstream fin("C:\\Users\\Harry\\Desktop\\B-large.in");
	int t;
	cin>>t;
	string buff;
	getline(cin, buff);
	for(int tc = 1; tc <=t; tc++){
		string str;
		cin>>str;
//		cout<<str<<endl;
		int res = 0;
		if(str[str.length()-1] == '-')
			res++;

		int i=0;
		int flag = 0;
		while(i<str.length()){
			if(str[i] == '+'){
				while(str[i] == '+'){
					i++;
					if(i>=str.length()){
						flag = 1;
						break;
					}
				}
				if(!flag)
					res++;
			}
			else{
				while(str[i] == '-'){
					i++;
					if(i>=str.length()){
						flag = 1;
						break;
					}
				}
				if(!flag)
					res++;
			}
		}


//		cout<<res<<endl;
		cout<<"Case #"<<tc<<": "<< res<<endl;
	}

	fout.close();
	return 0;
}
