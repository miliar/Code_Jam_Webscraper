#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
using namespace std;
/*
void mowRow( vector < vector < int > > &v, int n,  int s){
  for(int i=0; i<v[n].size(); i++)
    if(v[n][i]>s)
      v[n][i]=s;
}

void mowCol( vector < vector < int > > &v, int n, int s){
  for(int i=0; i<v.size(); i++)
    if(v[i][n]>s)
      v[i][n]=s;
}
void printv(vector < vector < int > > v){
  for(int i=0; i<v.size(); i++){
    for(int j=0; j<v[0].size(); j++)
      cout<<v[i][j]<<'\t';
    cout<<'\n';
  }
  cout<<'\n';
}*/

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

    /* vector < vector < int > > v;
  for(int i=0; i<10; i++){
  vector<int> tmp;
  for(int j=0; j<9; j++)
  tmp.push_back(100);
  v.push_back(tmp);
  }
  for(int i=0; i>=0; i++)
  {
  int rndrow=abs(((999999-245)*((1245635*i)%45)/(456))%10);
  int rndsize=abs(((29292659-245)*((1245635+i)%45)/(456))%13)+1;
  printv(v);
  mowRow(v,rndrow,rndsize);
  printv(v);
  rndsize=abs(((150125980-245)*((1245635+10*i)%45)/(456))%18)+1;
  rndrow=abs(((1505641545-245)*((1245635*i)%45)/(456))%9);
  mowCol(v,rndrow,rndsize);    
  }*/

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