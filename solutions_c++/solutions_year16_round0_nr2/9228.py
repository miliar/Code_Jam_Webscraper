#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int n,tc=1;
string s;

int main(){
  cin>>n;
  while(n--){
    cin>>s;
    char ch = '+';
    int c=0;
    for(int i=s.size()-1;i>=0;i--){
      if(ch!=s[i]){ 
        c++;
        ch=s[i];
      }
    }
    cout<<"Case #"<<(tc++)<<": "<<c<<endl;
    
  }

  return 0;
}

