#include <iostream>
#include <cstdio>
using namespace std;
void solve(int n){
  int smax;
  string s;
  cin >> smax >> s;
  int nowstanding  = s[0] - '0';
  int ans = 0;
  for(int i = 1; i <=smax;i++ ){
    int now = s[i] - '0' ;
    if(nowstanding < i){
      ans += i - nowstanding;
      nowstanding += i - nowstanding;
    }
    nowstanding += now;
  }
  printf("Case #%d: %d\n",n,ans);
}
int main(){
  int T ;
  cin >> T;
  for(int i = 0; i < T ; i++)solve(i+1);
}
