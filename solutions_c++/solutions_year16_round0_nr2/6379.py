#include <iostream>
#include <fstream>
#include <string>
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

string flip_string(string input_string){
	string result_string=input_string;
	int n=input_string.size();
	for(int i=0;i<n;i++){
		result_string[i]=input_string[n-i-1]=='+'?'-':'+';
	}
	return result_string;
}

int main () {
  string line;
  ifstream myfile ("B-large.in");
  ofstream result_file;
  result_file.open("q2_result_large.txt");
  if (myfile.is_open()){
  	getline(myfile,line);
  	int t=stoi(line);
    for(int i=0;i<t;++i){
	  getline (myfile,line);
      int flip_ct=0;
      char target_face='+';
      for(int j=line.size()-1;j>=0;--j){
      	if(line[j]!=target_face){
      		line=line.substr(0,j+1);
      		line=flip_string(line);
      		if(line[j]!=target_face){
      			//in this case we have to move on and focus on the other one
      			target_face=target_face=='+'?'-':'+';
			}
			//add one in either case
	  		flip_ct+=1;
    		
 		}
	  }
  	  result_file<<"Case #"<<i+1<<": "<<flip_ct<<"\n";
    }
    myfile.close();
    result_file.close();
  }
  return 0;
}
