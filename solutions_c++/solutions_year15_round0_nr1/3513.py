#include <iostream>
#include<string.h>
#include<cstdio>
using namespace std;

int main()
{
  freopen("in","r",stdin);
  freopen("out","w",stdout);

 int test;
 cin >> test;
 string str;
 long sMax;
 int t = 0;
 while(test--) {
  cin >> sMax >> str;
  long fNeed = 0;
  long temp;
  long count =(( str[0])-'0');
 for(long i = 1; i <= sMax; i++) {
  if( i > count && str[i] != '0')
 {  temp = i - count;
    fNeed += temp;
  }
 count += temp + ((str[i])-'0'); 
 temp = 0;
 }
 
/* if (sMax > count)
   sMax -= count;
  else
   sMax = 0;*/
 t++;
  cout << "Case #" << t << ": ";
  cout << fNeed << "\n";
 }

 return 0;
}
