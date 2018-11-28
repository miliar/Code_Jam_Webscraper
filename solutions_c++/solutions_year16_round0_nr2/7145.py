#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

int n;
string s;
vector<char> v;

void readData(){
   v.clear();
   cin>>s;
   for (int i = 0; i < s.size(); ++i){
      v.push_back(s[i]);
   }
}

int ok(){
   for (int i = 0; i < v.size(); ++i)
      if (v[i] == '-')
         return 0;
   return 1;
}

void printData(){
   int i = 0; n = 0;
   char c = v[0];
   for (i; i < v.size(); ++i)
      if (v[i] != c)
         break;
   while (i < v.size() || v[0] == '-'){
      n++;
      for (int j = i-1; j >= 0; --j){
         if (v[j] == '-')
            v[j] = '+';
         else
            v[j] = '-';
      }
      c = v[0];
      for (i; i < v.size(); ++i)
         if (v[i] != c)
            break;
   }
   printf("%d\n", n);
}

int main()
{
   freopen("data.in", "r", stdin);
   freopen("data.out", "w", stdout);
   int T, t;
   scanf("%d", &T);
   t = T;
   while (t--){
      readData();
      printf("Case #%d: ", T-t);
      printData();
   }

   return 0;
}
