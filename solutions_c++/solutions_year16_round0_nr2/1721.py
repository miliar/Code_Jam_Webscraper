#include <iostream>
#include <fstream>
using namespace std;

bool valid[10];

bool alreadyok(){
	for(int x=0; x<10; x++){
			if(!valid[x])return false;
	}
	return true;
}

void check(long long d){
	while(d>0){
		int aux = d/10*10;
		aux = d-aux;
		valid[aux]=true;
		d/=10;
	}
}

int main () {
  ofstream myfile;
  ifstream input;
  input.open("entrada.txt");
  myfile.open ("saida.txt");   
  int t;
  input>>t;
  for(int i=1; i<=t; i++){
		string s;
		int d = 0;
		input>>s;
		bool way = false;
		int op = 0;
		int x=0, y =s.size()-1;
		while(op<s.size() && y>=0){
			if(!way){
				if(s[y]=='-'){
					d++;
					way=!way;
				}
			}else{
				if(s[y]=='+'){
					way=!way;
					d++;
				}
			}
			y--;
			op++;
		}
		myfile<<"Case #"<<i<<": "<<d<<endl;
  }
  myfile.close();
  input.close();
  return 0;
}
