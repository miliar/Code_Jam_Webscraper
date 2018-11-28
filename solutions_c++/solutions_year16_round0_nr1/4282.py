#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <bits/stdc++.h>
#include <climits>
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
	ifstream fin("C:\\Users\\Harry\\Desktop\\A-large.in");
	int t;
	cin>>t;
	string buff;
	getline(cin, buff);

	unsigned long long int maxInt = ULLONG_MAX;
//	cout<<maxInt<<endl;
	for(int tc = 1; tc <=t; tc++){
//	for(long int tc=0; tc<=1000000; tc++){
		long int n,x;
		cin>>n;
//		n = tc;
		x = n;

		map<int,int> myMap;
//		cout<<n<<"::";
		if(n == 0){
			cout<<"Case #"<<tc<<": "<< "INSOMNIA"<<endl;
			continue;
		}

		unsigned long long int newNum = n;
//		cout<<"---newNum = "<<newNum<<endl;
		while(newNum>0 && newNum<maxInt){
//			cout<<"---newNum = "<<newNum<<endl;
			int dig = newNum%10;
			newNum/=10;
//			cout<<"---dig = "<<dig<<endl;
			if(myMap.find(dig) == myMap.end()){
				myMap.insert(make_pair(dig,dig));
//				cout<<"\t inserting "<<dig<<endl;
			}
		}
//		cout<<"myMapSize = "<<myMap.size()<<" n="<<n<<endl;
		while(myMap.size() < 10 && n<maxInt){
			n+=x;
			int newNum = n;
			while(newNum>0){
				int dig = newNum%10;
				newNum/=10;
				if(myMap.find(dig) == myMap.end()){
					myMap.insert(make_pair(dig,dig));
//					cout<<"\t inserting "<<dig<<endl;
				}
			}
//			cout<<"myMapSize = "<<myMap.size()<<" n="<<n<<endl;
		}
		cout<<"Case #"<<tc<<": "<< n<<endl;
	}

	fout.close();
	return 0;
}
