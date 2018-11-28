#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main() {
   int T,cnt, K,C,S;
   cin>> T;
   cnt = 1;
   while (T--) {
      cin >> K >> C>> S;
      cout <<"Case #" <<cnt++<< ":";
      for(int i = 1; i <= K ; i++)
         cout <<' '<< i ;
      cout <<endl;
   }

   return 0;


}
