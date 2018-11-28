#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string.h>
using namespace std;
bool isp(long long a){
  string s;
  for(;a>0;a/=10){
    s += char('0' + a%10);
  }
  bool f = true;
  for(int i = 0; i < (int) s.length()/2; i ++){
    if(s[i] != s[s.length()-1-i]){
      f = false;
      break;
    }
  }
  return f;
}
int solve(long long a,long long b){
  int ans = 0;
  for(long long i = 0; i <= 1200; i ++){
    string s="";
    for(int j = 0; j < 10; j ++){
      long long tmp = i;
      long long sq = i*10+j;
      for(;tmp>0;tmp/= 10){
        sq*= 10;
        sq+=tmp%10;
      }
      long long sq2 = sq*sq;
      if(isp(sq2)&&(a <= sq2)&&(sq2 <= b)){
        ans ++;
      }
    }
    long long sqb = i;
    long long tmp=i;
    for(;tmp>0;tmp/= 10){
      sqb*= 10;
      sqb+=tmp%10;
    }
    long long sq2b = sqb*sqb;
    if(isp(sq2b)&&(a <= sq2b)&&(sq2b <= b)){
        ans ++;
  //      cout << sq2b<<endl;;
    }
  }
  return ans;
}
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int qwe = 0; qwe < t; qwe ++){
      long long a,b;
      scanf("%I64d%I64d",&a,&b);
      printf("%s%d%s%d\n","Case #",qwe+1,": ",solve(a,b));
    }
}
