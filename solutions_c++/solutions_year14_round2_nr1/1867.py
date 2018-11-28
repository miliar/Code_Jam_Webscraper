#include<bits/stdc++.h>
using namespace std;
vector<string> in;
bool input(){
  int n;
  cin>>n;
  in.resize(n);
  for(int i=0;i<n;i++){
    cin>>in[i];
  }
  return true;
}
void solve(){
  cerr<<endl;
  string last=in[0].substr(0,1);
  for(int i=1;i<in[0].size();i++){
    if(last[last.size()-1]!=in[0][i]){
      last=last+in[0][i];
    }
  }
  for(int i=0;i<in.size();i++){
    string tmp = in[i].substr(0,1);
    for(int j=1;j<in[i].size();j++){
      if(tmp[tmp.size()-1]!=in[i][j]){
        tmp=tmp+in[i][j];
      }
    }
    if(last!=tmp){
      cout<<"Fegla Won"<<endl;
      return;
    }
  }
  vector<vector<int>> each_num(last.size(),vector<int>(in.size(),0));
  for(int i=0;i<in.size();i++){
    int k=0;
    for(int j=0;j<in[i].size();j++){
      if(in[i][j]==last[k]){
        each_num[k][i]++;
      }else{
        k++;
        if(in[i][j]==last[k]){
          each_num[k][i]++;
        }
      }
    }
  }
  int ans=0;
  for(int i=0;i<each_num.size();i++){
    cerr<<i<<":";
    int tmp=0;
    for(int j=0;j<each_num[i].size();j++){
      cerr<<each_num[i][j]<<" ";
      tmp+= each_num[i][j];
    }cerr<<endl;
    tmp/=each_num[i].size();
    cerr<<"tmp::"<<tmp<<endl;
    int tttmp=0;
    int ttmp=0;
    for(int j=0;j<each_num[i].size();j++){
      ttmp += abs(each_num[i][j]-tmp);
    }
    for(int j=0;j<each_num[i].size();j++){
      tttmp += abs(each_num[i][j]-(tmp+1));
    }
    ans+= min(ttmp,tttmp);
  }
  cout<<ans<<endl;
}

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    input();
    cout<<"Case #"<<i+1<<": ";
    solve();
  }
}
