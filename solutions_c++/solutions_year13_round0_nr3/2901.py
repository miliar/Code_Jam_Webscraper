#include<iostream>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<math.h>


using namespace std;

bool chk(long long a) {
  stringstream hv; hv<<a;
  string s=hv.str();
  for(int i=0;i<s.length();i++)
    if(s[i]!=s[s.length()-1-i])
      return false;
  return true;
}

int main(int argc, char *argv []) {
  if(argc<3) return 1;
  ifstream input;
  input.open(argv[1]);
  ofstream output;
  output.open(argv[2]);
  int tcc;
  string nummern;
  getline(input,nummern);
  stringstream(nummern)>>tcc;
  for(int testnr=1;testnr<=tcc;testnr++) {
    long long A,B;
    getline(input,nummern);
    stringstream(nummern)>>A>>B;
    long long res=0;
    for(long long p=sqrt(A)-1;p<sqrt(B)+2;p++)
      if(p*p>=A&&p*p<=B)
        if(chk(p)&&chk(p*p)) res++;
    output<<"Case #"<<testnr<<": "<<res<<endl;
  }
  input.close();
  output.close();
  cout<<"\nFinished\n";
  return 0;
}
