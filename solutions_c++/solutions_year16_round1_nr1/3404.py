#include<bits/stdc++.h>
using namespace std;

int main(){
  int n,slen,maxc;
  list<char> l;
  string s;
  cin>>n;
  for(int i=0;i<n;i++){
    cin>>s;
    l.push_back(s[0]);
    slen=s.size();
    maxc=s[0];
    for(int j=1;j<slen;j++){
      if(l.front()>s[j])l.push_back(s[j]);
      else if(l.front()<s[j])l.push_front(s[j]);
      else if(l.front()==s[j]){
	if(maxc>s[j])l.push_back(s[j]);
	else l.push_front(s[j]);
      }
      maxc=s[j];
    }
    cout<<"Case #"<<i+1<<": ";
    while(l.size()){
      cout<<l.front();
      l.pop_front();
    }
    cout<<endl;
  }
  return 0;
}
