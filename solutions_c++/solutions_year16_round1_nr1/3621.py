#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


int stoi(string s){
	int n=s.size();
	int result=0;
	int i;
	if(s[0]!='-'){
		i=0;
	}else{
		i=1;
	}
	for(i;i<n;++i){
		result=result*10+s[i]-'0';
	}
	if(s[0]=='-'){
		result=-result;
	}
	return result;
}

vector<string> string_split(string s,char c){
	vector<string> result;
	string tmp="";
	for(int i=0;i<s.size();i++){
		if(s[i]==c){
			if(tmp!=""){
				result.push_back(tmp);
				tmp="";
			}
		}else{
			tmp=tmp+s[i];
		}
	}
	if(tmp!=""){
		result.push_back(tmp);
	}
	return result;
}

string alsort(string s){
	int n=s.size();
	string result;
	result.push_back(s[0]);
	for(int i=1;i<n;++i){
		if(s[i]-result[0]>=0){
			result=s[i]+result;
		}else if(s[i]-result[0]<0){
			result.push_back(s[i]);
		}
	}
	return result;
}

int main () {
  string line;
  ifstream myfile ("A-large.in");
  ofstream result_file;
  result_file.open("q1_result.txt");
  if (myfile.is_open()){
  	getline(myfile,line);
  	int t=stoi(line);
    for(int i=0;i<t;++i){
	  getline (myfile,line);
	  
	  result_file<<"Case #"<<i+1<<": ";
  	  result_file<<alsort(line)<<"\n";
    }
    myfile.close();
    result_file.close();
  }
  return 0;
}
