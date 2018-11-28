#include<iostream>
#include<fstream>
#include<sstream>
#include<algorithm>

using namespace std;

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
  char voc[5]={'a','e','i','o','u'};
  for(int testnr=1;testnr<=tcc;testnr++) {
    getline(input,nummern);
    string s; int n;
    stringstream ss(nummern);
    ss>>s>>n;
    long long res=0;
    int lastnr=-1;
    for(int i=0;i+n<=s.length();i++) {
      bool nw=true;
      for(int r=0;r<n&&nw;r++) {
        for(int k=0;k<5&&nw;k++)
          nw=(s[i+r]!=voc[k]);
      }
      if(nw) {
        long long hv=i-lastnr;
        res+=hv*(s.length()-i-(n-1));
        lastnr=i;
      }
    }
    output<<"Case #"<<testnr<<": "<<res<<endl;
  }
  input.close();
  output.close();
  cout<<"\nFinished\n";
  return 0;
}
