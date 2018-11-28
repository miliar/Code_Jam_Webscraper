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
		long long n;
		long long d;
		input>>n;
		for(int x=0; x<10; x++){
			valid[x]=false;
		}
		if(n==0)myfile<<"Case #"<<i<<": INSOMNIA"<<endl;
		else{
			d = n;
			while(!alreadyok()){
				check(d);
				if(alreadyok())break;
				d+=n;
			}
		if(alreadyok()){
			myfile<<"Case #"<<i<<": "<<d<<endl;
		}else {
			myfile<<"Case #"<<i<<": INSOMNIA"<<endl;
		}
		}
  }
  myfile.close();
  input.close();
  return 0;
}
