#include <iostream>     // std::cout
#include <fstream>      // std::ifstream
#include <vector> 
#include <string>     // std::string, std::stoi
#include <unordered_set>
#include <stdlib.h>
using namespace std;

string check(string s){
	if(stol(s)==0)return "INSOMNIA";
	unordered_set<int>record;
	int j = 2;
	int end = 1;
	string curr = s;
	while(end){
		for(int i=0;i<curr.size();i++){
			if(curr[i]<='9'&&curr[i]>='0'){
				int cur = curr[i]-'0';
				if(record.find(cur)==record.end()){
				record.insert(cur);
				if(record.size()==10){
					end = 0;
					break;
				}
				}
			}
		}
		 curr= to_string(j*stol(s));
		 //cout<<curr<<endl;
		 j++;
	}
	return to_string((j-2)*stol(s));;
}


void parsefile(char* infile,vector<string>&test){
	ifstream input;
	input.open(infile,ifstream::in);
	string tmp;
	int row_cnt = 0;
	while(getline(input,tmp)){
		
		//cout<<tmp<<endl;
		if(row_cnt >0){
			test.push_back(tmp);
		}
		row_cnt++;
	}
}


int main(int argc,char* argv[]){
	
	char* infile = argv[1];
	vector<string>test;
	parsefile(infile,test);
	// for(int i=0;i<test.size();i++){
	//  	cout<<test[i]<<endl;
	// }
	
	//cout<<"A"<<endl;
	for(int i=0;i<test.size();i++){
		string num = check(test[i]);
		cout<<"Case #"<<i+1<<": "<<num<<endl;
	}
	//cout<<"END"<<endl;
	return 1;

}