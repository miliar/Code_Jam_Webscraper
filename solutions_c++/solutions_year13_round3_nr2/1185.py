#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<map>
#include<vector>
#include<deque>
using namespace std;
#define ull unsigned long long
int T,a,b,d;
string ans;
int x,y;
int main(){
  cin>>T;
  for(int tc=1;tc<=T;tc++){
    printf("Case #%d: ",tc);
    cin>>a>>b;
    ans="";
    x=y=0;
    while(x<a){
      x++;
      ans+='W';
      ans+='E';
    }
    while(x>a){
      x--;
      ans+='E';
      ans+='W';
    }
    while(y<b){
      y++;
      ans+='S';
      ans+='N';
    }
    while(y>b){
      y--;
      ans+='N';
      ans+='S';
    }
    cout<<ans<<endl;
  }
  return 0;
}
