#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string>
#include <sstream>
using namespace std;
bool is_palindrome(string &str);
int main() {
  int ntc;
  stringstream ss;
  string str1,str2;
  long long a,b;
  long long npal;
  scanf("%d\n",&ntc);
  for(int tc=1;tc<=ntc;++tc) {
    npal=0;
    scanf("%lld %lld\n",&a,&b);
    long long left=ceil( sqrt((double) a) );
    long long right=floor( sqrt((double) b) );
    for(int i=0;i<right-left+1;++i) {
      ss<<left+i;
      str1=ss.str();
      ss.str(std::string());
      ss<<pow(left+i,2);
      str2=ss.str();
      ss.str(std::string());
      if(is_palindrome(str1) && is_palindrome(str2)) {
        npal++;
      }
    }
    printf("Case #%d: %lld\n",tc,npal);
  }
  return 0;
}
bool is_palindrome(string &str) {
  int size=str.size();
  for(int i=0;i<=size/2;i++) {
    if(str[i]!=str[size-i-1]) return false;
  }
  return true;
}
