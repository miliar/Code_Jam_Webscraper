#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main() {
   int T, c, cnt;
   char pan[101];
   cin>> T;
   c = 0;
   while (T--) {
   c++;
   cin>> pan;
   cnt = 0;
   int len = strlen(pan);

   char prev = pan[0];
   for (int i = 1; i< len; i++) {
      if (prev != pan[i]) {
         prev = pan[i];
         cnt++;
      }
   }
   if (pan[len-1] == '-')
      cnt++;
   cout <<"Case #"<<c<<": "<< cnt<<endl;
   }
   return 0;
}
