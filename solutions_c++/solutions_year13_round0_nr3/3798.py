#include <cstdio>
#include <sstream>
#include <fstream>
#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int isPS[1001];
bool isPal(int x){
  stringstream ss;
  ss << x;
  string s;
  ss >> s;
  string t = s;
  int n = s.length();
  for(int i=0;i<n;++i) if(s[i]!=s[n-i-1]) return 0;
  return 1;
}
void furui(){
  for(int i=1;i*i<=1000;++i) if(isPal(i) && isPal(i*i)) isPS[i*i] = 1;
}
int main(){
  furui();
  int T;
  scanf("%d",&T);
  for(int i=1;i<=T;++i){
    int cnt = 0;
    int a,b;
    scanf("%d%d",&a,&b);
    for(int j=a;j<=b;++j) cnt+=isPS[j];
    printf("Case #%d: %d\n",i,cnt);
  }
  return 0;
}
