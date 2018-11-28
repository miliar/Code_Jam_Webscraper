#include <stdio.h>
#include <string>

using namespace std;

int T,TT;
int n,p,r,s,m;
int found;

char winner(char x, char y){
  if(x=='R' && y=='S')return x;
  if(y=='R' && x=='S')return y;
  if(x=='S' && y=='P')return x;
  if(y=='S' && x=='P')return y;
  if(x=='P' && y=='R')return x;
  if(y=='P' && x=='R')return y;
  return 0;
}

int back(string str){
  int i;
  if(str.size()==m){
    int P,R,S;
    string str1,str2;
    P=R=S=0;
    for(i=0;i<str.size();i++){
      P+=(str[i]=='P');
      R+=(str[i]=='R');
      S+=(str[i]=='S');
    }
    if(P==p && R==r && S==s){
      str1=str;
      while(str1.size()>1){
        str2="";
        for(i=0;i<str1.size();i+=2){
          if(str1[i]==str1[i+1])return 0;
          str2+=winner(str1[i],str1[i+1]);
        }
        str1=str2;
      }
      printf("%s",str.c_str());
      return 1;
    }
    return 0;
  }
  if(back(str+"P"))return 1;
  if(back(str+"R"))return 1;
  if(back(str+"S"))return 1;
  return 0;
}

int main() {
  scanf("%d",&TT);
  for(T=1;T<=TT;T++){
    scanf("%d%d%d%d",&n,&r,&p,&s);
    printf("Case #%d: ",T);
    m=1<<n;
    found=0;
    if(!back(""))printf("IMPOSSIBLE");
    printf("\n");
  }
  return 0;
}
