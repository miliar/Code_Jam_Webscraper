#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
using namespace std;

bool checklawn(vector< vector <int > > lawn){
  int n=lawn.size(), m=lawn[0].size();
  for(int j=0; j<n; j++){
    int mx=*max_element(lawn[j].begin(),lawn[j].end());
    for(int k=0; k<m; k++)
      if(lawn[j][k]<mx)
        for(int l=0; l<n; l++)
          if(lawn[l][k]>lawn[j][k])
            return 0;
  }
  return 1;
}

int main(){

  ifstream infile ("input.in");
  ofstream outfile("output.out");
  int c,n,m,r;
  infile>>c;
  for(int i=0; i<c; i++){
    infile>>n>>m;
    vector< vector<int> > lawn;
    for(int j=0; j<n; j++){
      vector<int> row;      
      for(int k=0; k<m; k++){
        infile>>r;
        row.push_back(r);
      }
      lawn.push_back(row);
    }
    if (checklawn(lawn)==1)
      outfile<<"Case #"<<i+1<<": "<<"YES"<<endl;
    else
      outfile<<"Case #"<<i+1<<": "<<"NO"<<endl;
  }
}