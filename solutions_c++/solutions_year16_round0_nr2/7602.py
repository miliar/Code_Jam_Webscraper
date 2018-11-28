#include<iostream>
#include<string>

using namespace std;

int main(void) {
   FILE *input = freopen("input.txt", "r", stdin);
   FILE *output = freopen("output.txt", "w+", stdout);
   int testcase;
   scanf("%d", &testcase);
   
   for (int i = 0; i < testcase; i++) {
      string s;
      cin >> s;
      int count = 0;
      for (int i = 0; i < s.size() - 1; i++) {
         if (s[i] != s[i + 1])
            count++;

      }
      if (s[s.size() - 1] == '-')
         count++;

      printf("Case #%d: %d\n", i + 1, count);
   }
      

   
      
   
   return 0;
}