#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main(int argc, char** argv){
  ofstream outfile("out.txt");
  ifstream inp(argv[1]);
  string line;
  int T;
  inp>>T;
  getline(inp,line);
  for(int t=1;t<=T;t++){
    getline(inp,line);
    cout<<line<<endl;
    int count=0;
    int cont = 0;
    for(int i=0;i<line.length();i++){
        if(line[i]=='-' && cont==0){
          count++;
          cont=1;
        }
        else if(line[i]=='+'){
          cont=0;
        }
    }
    int res = 2*count;
    if(line[0]=='-')res--;
    outfile<<"Case #"<<t<<": "<<res<<endl;
  }
}
