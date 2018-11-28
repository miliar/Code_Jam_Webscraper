#include <iostream>
#include <string.h>
#include <ctype.h>
using namespace std;

int main(){
  int t,q;
  long long i,h,s,m;
  string p,c,temp;
  cin>>t;
  q=t;
  while(t--){
    cin>>p;
    m=0;
    c="";
    for(i=0;i<p.length();i++) c+='+';
    while(p!=c){
      h=s=i=0;
      temp="";
      while(p[i]=='+' && i<p.length()){
        h++;
        i++;
      }
      i=0;
      while(p[i]=='-' && i<p.length()){
        s++;
        i++;
      }
      if(h==0){
        for(i=0;i<s;i++) temp+='+';
        p=temp+p.substr(s,p.length()-s);
      }
      else if(s==0){
        for(i=0;i<h;i++) temp+='-';
        p=temp+p.substr(h,p.length()-h);
      }
      m++;
    }
    cout<<"Case #"<<q-t<<": "<<m<<endl;
  }
  return 0;
}
