#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

string foo(string S){
  int slen = S.length();
  if(slen == 0 || slen == 1)
    return S;

  int maxi = -1, first_maxi = -1;
  char maxc = '0';
  for(int i = 0; i < slen; i++) {
    if(S[i] > maxc) {
      maxi = i;
      maxc = S[i];
    }
  }

  //cout<<maxc<<"@"<<maxi<<endl;
  vector<int> maxc_pos;
  for(int i = 0; i < slen; i++)
    if(S[i] == maxc) {
      first_maxi = i;
      break;
    }


  string post = "";
  string maxcs = "";
  maxcs += S[first_maxi];
  int maxc_count = 0;
  for(int i = first_maxi + 1; i < slen; i++)
    if(S[i] != maxc) post += S[i];
    else maxcs += S[i];

  return maxcs + foo(S.substr(0, first_maxi)) + post;
}

int main(){
  ofstream fout;
  ifstream fin;
  fin.open("A-large.in");
  fout.open("Ab.out");
  
  //cout<<"open success\n";
  
  int T = 0;
  fin>>T;
  
  //cout<<"input size success\n";
  
  for(int i=0;i<T;i++){
    fout<<"Case #"<<i+1<<": ";
    string S;
    fin>>S;
    //code here 
    fout<<foo(S);

    //code end
    fout<<endl;
  }

}