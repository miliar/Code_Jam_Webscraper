#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<string>
#include<sstream>
#include<unordered_map>

using namespace std;

int main(){
  int T;
  cin>>T;
  for(int c=1;c<=T;c++){
    int N;
    cin>>N;
    cin.ignore(99,'\n');
    unordered_map<string,int> bt;
    for(int i=0;i<N;i++){
      string s;
      getline(cin,s);
      stringstream ss(s);
      for(string t;ss>>t;){
	bt[t]|=1<<i;
      }
    }
    int ans=1e9;
    for(int i=2;i<1<<N;i+=4){
      int ri=~i;
      int c=0;
      for(const auto &e:bt){
	c+=(e.second&i)&&(e.second&ri);
      }
      ans=min(ans,c);
    }
    cout<<"Case #"<<c<<": "<<ans<<endl;
  }
}

