#include<iostream>
#include<vector>
#include<climits>
#include<sstream>
using namespace std;

#define MAX 100000000000100

vector<long long> list;
bool rev(long long i){
  stringstream ss;
  ss<<i;
  string s;
  ss>>s;
  for(int i=0;i<s.size();i++){
    if(s[i]!=s[s.size()-1-i]){
      return false;
    }
  }
  return true;
}
void make_list(){
  for(long long i=1;i*i<MAX;i++){
    long long tmp=i*i;
    if(rev(i)&&rev(tmp)){
      list.push_back(tmp);
    }
  }
}
int solve(){
  int a,b;
  cin>>a>>b;
  int ans=0;
  for(int i=0;i<list.size();i++){
    if(list[i]>b){
      break;
    }
    if(list[i]>=a){
      ans++;
    }
  }
  return ans;
}


int main(){
  make_list();
  /*
  for(int i=0;i<list.size();i++){
    cout<<list[i]<<" ";
  }cout<<endl;
  */
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    cout<<"Case #"<<i+1<<": "<<solve()<<endl;    
  }
}
