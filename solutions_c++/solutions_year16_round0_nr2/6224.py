#include <iostream>
#include <string.h>
#include<cstdio>
#include <algorithm>
using namespace std;
int check(string s){
  for(int i=0;i<s.length();i++){
    if(s[i]!='+') return 0;
  }
  return 1;
}
string func(int i,string s){
  for(int j=0;j<=i;j++){
    if(s[j]=='-') s[j]='+';
    else s[j]='-';
  }
  return s;
}
int main() {
  int t;
  scanf("%d",&t);
for(int k=1;k<=t;k++)
    {
    string s;
    cin>>s;
    int n=0;
    int p=s.length()-1;
    for(int i=p;i>=0;i--){
      if(check(s) == 1) break;
      if(s[i]=='-'){
        s=func(i,s);
        n++;
      }
    }
    printf("Case #%lld: ",k);
    cout<<n;
    if(k!=t)
      printf("\n");
    }
    return 0;
  }
