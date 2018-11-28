#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

map<string,vector<int>> loc;
vector<vector<int>> cp;

vector<bool> vec;
int N;
int sol;


int count(){
  int co=0;
  for(auto& c:cp){
    bool b = vec[c[0]];
    for(int se:c){
      bool bb=vec[se];
      if(bb!=b){
	co++;
	break;
      }
    }
  }
  return co;
}

bool recur(int lev){
  if(lev==N){
    sol=min(sol,count());
  }else{
    vec[lev]=false;
    recur(lev+1);
    vec[lev]=true;
    recur(lev+1);
  }
}


int solve(){
  loc.clear();
  vec.clear();
  cin>>N;
  vec.resize(N);
  vec[0]=true;
  vec[1]=false;
  string line;
  getline(cin,line);
  for(int i=0;i<N;i++){
    getline(cin,line);
    stringstream linestream(line);
    string word;
    while(linestream>>word){
      loc[word].push_back(i);
    }
  }
  cp.clear();
  for(auto& n:loc)
    cp.push_back(n.second);
  sol=10000;
  recur(2);
  return sol;
}


int main(){
  int cases;
  cin>>cases;
  for(int i=0;i<cases;i++){
    cout<<"Case #"<<i+1<<": "<<solve()<<endl;
  }
  return 0;
}
