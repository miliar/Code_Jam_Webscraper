#include <iostream>
#include <fstream>
using namespace std;

int main () {
  ofstream myfile;
  ifstream input;
  input.open("entrada.txt");
  myfile.open ("saida.txt");   
  int t;
  input>>t;
  for(int i=1; i<=t; i++){
		int k, c, s;
		input>>k>>c>>s;
		myfile<<"Case #"<<i<<": 1";
		for(int j=2; j<=s; j++){
			myfile<<" "<<j;
		}
		myfile<<endl;
  }
  myfile.close();
  input.close();
  return 0;
}
