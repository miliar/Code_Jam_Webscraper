#include <bits/stdc++.h>
using namespace std;
int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    string s;
    cin>>s;
    int len=s.length();
    list<char> ls;
    ls.push_back(s[0]);
     for(int j=1;j<len;j++){
       if(ls.front()<=s[j])
        ls.push_front(s[j]);
      else
        ls.push_back(s[j]);

     }
     list<char>::iterator it=ls.begin();
     cout<<"Case #"<<i+1<<": ";
     for(;it!=ls.end();it++)
      cout<<*it;
    cout<<"\n";
  }
}
