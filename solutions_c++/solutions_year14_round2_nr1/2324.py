//============================================================================
// Name        : Codejam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;

struct compare {
	bool operator()(const std::string& first, const std::string& second) {
		return first.size() > second.size();
	}
};

int main() {
	bool impossible;
	int t,T,n,i,charcount[102],curcharpointer[102],totalCharCount,totalNumMoves;
	char curchar,curcharindex;
	vector<string> str;
	string tempstr;
	cin>>T;
	for(t=1;t<=T;++t){
		totalNumMoves=0;
		impossible=0;

		str.clear();
		cin>>n;
		for(i=0;i<n;++i){
			cin>>tempstr;
			str.push_back(tempstr);
		}

		while(1){
			memset(charcount,0,sizeof(charcount));
			std::sort(str.begin(),str.end(),compare());
			if(str[0].size()==0) break;
			curchar=str[0][0];
			totalCharCount=0;
			//cout<<"Cur char="<<curchar<<endl;
			for(i=0;i<str.size() && !impossible;++i){

				while(str[i].size()>0 && str[i][0]==curchar){
				//	cout<<"Found one "<<curchar<<" in string"<<i<<endl;
					str[i].erase(str[i].begin());
					++charcount[i];
					++totalCharCount;
				}
				if(charcount[i]==0) impossible=1;
			}

			if(impossible){
				cout<<"Case #"<<t<<": Fegla Won"<<endl;
				break;
			}
			int avg=totalCharCount/n;
			for(i=0;i<str.size();++i){
				//cout<<"Average ="<<avg<<" charcount[i]="<<charcount[i]<<endl;
				totalNumMoves+=abs(avg-charcount[i]);
			}

		}
		if(impossible) continue;


		cout<<"Case #"<<t<<": "<<totalNumMoves<<endl;
	}
	return 0;
}
