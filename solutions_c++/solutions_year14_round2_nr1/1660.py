#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;
int tc;
int n,ans;
string temp;
string inps[111];
string reduce(string x){
  std::string ret = x.substr(0,1);
 // cout<<x<<" --  "<<ret<<endl;
  for(int i=1;i<x.size();i++){
    if(x[i]!=x[i-1])ret+=x[i];
  }
  return ret;
}
int cc(int i,char a){
  int skipcnt=0;
  string rep="";
  bool skip=true;
  for(int k=0;k<inps[i].size();k++){
    if(skip&&inps[i][k]!=a)skip=false;
    if(!skip)rep+=inps[i][k];
    else skipcnt++;
  }
  inps[i]=rep;
  return skipcnt;
}
int getEqCost(int eq,vector<int> nums){
  int cost=0;
  for(int i=0;i<nums.size();i++){
    cost+=abs(eq-nums[i]);
  }
  return cost;
}
int match(char a){
  vector<int> m;
  for(int i=0;i<n;i++){
    m.push_back(cc(i,a));
  }
  int cur=10000000;
  for(int i=0;i<m.size();i++){
    cur=min(cur,getEqCost(m[i],m));
  }
  return cur;
}
int main(){
  cin>>tc;
  for(int tcc=1;tcc<=tc;tcc++){
    cout<<"Case #"<<tcc<<": ";
    cin>>n;
    bool ok=true;
    ans=0;
    for(int i=0;i<n;i++)cin>>inps[i];
    temp=reduce(inps[0]);
    for(int i=1;i<n;i++){
      if(temp!=reduce(inps[i])){
        ok=false;
        break;
      }
    }
    int ta;
    if(ok){
      //cout<<endl<<temp<<endl;
      for(int i=0;i<temp.size();i++){
        ans+=match(temp[i]);
      }
      cout<<ans<<endl;
    }else{
      cout<<"Fegla Won\n";
    }
  }
  return 0;
}
