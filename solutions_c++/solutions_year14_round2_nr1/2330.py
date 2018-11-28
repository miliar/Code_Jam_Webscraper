#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;


int main(int argc, char **argv) {
  int T, N, i, j, k, l, y;
  cin>>T;
  for(int c=1; c<=T; c++) {
    cin>>N;
    vector<string> str(N);
    for(i=0; i<N; i++)
      cin>>str[i];
    
    string motif=str[0];
    string::iterator end = unique(motif.begin(), motif.end());
    motif.resize(distance(motif.begin(), end));
    
    vector< vector<int> > mtr(N, vector<int>(motif.size()));
    bool np=false;
    for(i=0; i<str.size() && !np; i++) {
      string& stri = str[i];
      k=0;
      for(j=0; j<motif.size() && !np; j++) {
	l=k;
	while(k<stri.size() && stri[k]==motif[j]) k++;
	np = (k-l==0 || ((j+1)==motif.size() && k<stri.size()));
	mtr[i][j]=k-l;
      }
    }
    
    if(np) {
      cout<<"Case #"<<c<<": Fegla Won"<<endl;
    }
    else {
      y=0;
      for(j=0; j<motif.size(); j++) {
	int mean=0;
	for(i=0; i<mtr.size(); i++) {
	  mean += mtr[i][j];
// 	  cout<<mtr[i][j]<<" ";
	}
// 	cout<<endl;
	mean /= mtr.size();
	for(i=0; i<mtr.size(); i++)
	  y += abs(mtr[i][j] - mean);
      }
      cout<<"Case #"<<c<<": "<<y<<endl;
    }
  }
  return 0;
}
