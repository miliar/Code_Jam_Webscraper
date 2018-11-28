#include<iostream>
#include<fstream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

ifstream fin("in");
ofstream fout("out");

bool consonant(char c){
  return (c!='a' && c!='e' && c!='i' && c!='o' && c!='u');
}

int func(string L,int n){
  int st=0;
  for (string::iterator it=L.begin(); it<L.end(); it++){
    for (string::iterator itt=it; itt<L.end(); itt++){
      int dist=0;
      for (string::iterator ittt=it; ittt<=itt; ittt++){
	if (consonant(*ittt)){
	  dist++;
	} else {
	  dist=0;
	}
	if (dist>=n) {
	  st++;
	  break;
	}
      }
    }
  }
  return st;
}

int main(){
  int T, n, status;
  string L;
  fin >> T;
  for (int count=1; count<=T; count++){
    fin >>L>>n;
    fout<< "Case #"<<count<<": ";
    status=func(L,n);
    fout <<status<<endl;
  }
}
