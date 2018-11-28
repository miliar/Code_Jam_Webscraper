#include <iostream>     // std::cout
#include <fstream>      // std::ifstream
#include <vector> 
#include <string>     // std::string, std::stoi
#include <unordered_set>
#include <stdlib.h>
#include <algorithm>
using namespace std;
void parsefile(char* infile,vector<string>&test){
	ifstream input;
	input.open(infile,ifstream::in);
	string tmp;
	int row_cnt = 0;
	while(getline(input,tmp)){
		
		//cout<<tmp<<endl;
		if(row_cnt >0){
			test.push_back(tmp);
			//cout<<tmp<<endl;
		}
		row_cnt++;
	}
}


void flip(int n,string &cakes){
	reverse(cakes.begin(),cakes.begin()+n);
	for(int i=0;i<=n;i++){
		if(cakes[i]=='+')cakes[i]='-';
		else{
			cakes[i]='+';
		}
	}
}

int check(string cakes){
	int ans = 0;
	int sz = cakes.size();
	while(sz>count(cakes.begin(),cakes.end(),'+')){
		int i=0;
		while(cakes[i]==cakes[i+1]){
			i++;
		}
		if(i==cakes.size()-1&&cakes[i]=='+')break;
		flip(i,cakes);
		ans++;
	}
	return ans;
}



int main(int argc,char* argv[]){
	// string a = "-++-";
	// flip(3,a);
	// cout<<a<<endl;
	char* infile = argv[1];
	vector<string>test;
	parsefile(infile,test);
	// for(int i=0;i<test.size();i++){
	//  	cout<<test[i]<<endl;
	// }
	
	//cout<<"A"<<endl;
	for(int i=0;i<test.size();i++){
		//cout<<"t"<<test[i]<<endl;
		int num = check(test[i]);
		cout<<"Case #"<<i+1<<": "<<num<<endl;
	}
	
	return 1;

}