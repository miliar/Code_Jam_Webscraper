#include <bits/stdc++.h>
using namespace std;
int main()
{
  // freopen("out.txt","w",stdout);
   int test , cs = 1;
   cin >> test;
   while(test--){
      string s;
      cin >> s;
      char ch = s[0];
      string a , b;
      for(int i = 1 ; i< s.size() ; i++){
         if(s[i] >= ch){
             a += s[i];
             ch = s[i];
         }
         else b += s[i];
      }
     reverse(a.begin() , a.end());
     printf("Case #%d: ", cs++);
     cout << a << s[0] << b << endl;
   }

}
