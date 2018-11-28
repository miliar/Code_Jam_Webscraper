#include<bits/stdc++.h>
using namespace std;
int main(){
long long g=0;
cin>>g;
vector<long long>rsp;
for(long long u=0;u<g;u++){
  string p;
  cin>>p;
  vector<char>vec;
  for(long long i=0;i<p.size();i++){
    vec.push_back(p[i]);
  }
  char estado;
  long long tmp=0;
  estado=vec[0];
  for(int i=1;i<vec.size();i++){
    if(vec[i]!=vec[i-1]){tmp++;estado=vec[i];}
  }
  if(estado=='-'){tmp++;}
  rsp.push_back(tmp);
}
for(long long i=0;i<rsp.size();i++){
  cout<<"Case #"<<i+1<<": "<<rsp[i]<<endl;
}
}