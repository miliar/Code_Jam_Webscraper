#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

string up(string s, int i){
		if(i==0)return s;
		if(s[i]=='0'){
			s[i]='1';
			return s;
		}else{
			s[i]='0';
			return up(s, i-1);
		}	
}

ofstream myfile;
ifstream input;

bool test(string s){
	int a = 0;
	int b=1;
	for(int i=0; i<s.size(); i++){
		if(s[i]=='1'){
			a+=b;
		}
		b=-b;
	}
	if(a==0)return true;
	return false;
}

int main () {
  input.open("entrada.txt");
  myfile.open ("saida.txt");   
  int t;
  input>>t;
  for(int i=1; i<=t; i++){
		string s = "";
		string lim = "";
		int n, j;
		input>>n>>j;
		for(int k=0; k<n; k++){
			s+="0";
			lim += "1";
		}
		s[0]='1';
		s[s.size()-1]='1';
		int myops = 0;
		myfile<<"Case #"<<i<<":"<<endl;
		while(myops<j){
			
			if(test(s)){
				myops++;
				myfile<<s<<" "<<3<<" "<<4<<" "<<5<<" "<<6<<" "<<7<<" "<<8<<" "<<9<<" "<<10<<" "<<11<<endl;
			}
			//cout<<s<<"--"<<myops<<endl;
			s = up(s, s.size()-2);
			if(myops==j)break;
		}
		//cout<<myops<<endl;
		//myfile<<"Case #"<<i<<": "<<d<<endl;
  }
  myfile.close();
  input.close();
  return 0;
}
