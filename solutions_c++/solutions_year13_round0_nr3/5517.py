#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

char buf[4];

int palindrome(int p) {
  memset(buf,0,sizeof(char)*4);
  int t=true;
  sprintf(buf,"%d",p);
  int l=strlen(buf);
  for (int i=0;i<l/2;i++)
    if (buf[i]!=buf[l-1-i]) {
      t=false;
      break;
    }
  //if (t) cout<<buf<<endl;
  return t;
  //cout<<buf<<' '<<strlen(buf)<<endl;
}

int main(void) {
  int t=0,a=0,b=0,tt=0,ar=0,br=0,c=0;
  cin>>t;
  tt=t;
  while (t--) {
    c=0;
    cout<<"Case #"<<tt-t<<": ";
    cin>>a>>b;
    ar=sqrt(a);
    br=sqrt(b);
    if (ar*ar<a) ar++;
    //cout<<a<<' '<<b<<' '<<ar<<' '<<br<<' '<<endl;
    for (int i=ar;i<=br;i++) {
      if (palindrome(i)&&palindrome(i*i))
        c++;
    }
    cout<<c<<endl;
  }
  return 0;
}
