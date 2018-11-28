#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;
char ch[1200],p[1200];
int main(){
  int T;
  scanf("%d",&T);
  int cas;
  string a,b,res;
  a=b=res="";
  for(cas=1;cas<=T;cas++){
    scanf("%s",ch);
    int len= strlen(ch);
    a=b=res="";
    for(int i=0;i<len;i++){
      a=b=res;
      p[0]=ch[i];
      p[1]=0;
      string tep = p;
      a = tep + a;
      b = b + tep;
      if(a<b){
        res = b;
      } else {
        res = a;
      }
    }
    printf("Case #%d: %s\n",cas,res.c_str());
  }
  return 0;
}