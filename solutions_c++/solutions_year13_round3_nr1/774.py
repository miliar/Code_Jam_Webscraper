#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool cons(char x)
{
   static const char vowels[] = "aeiou";
   for(int i=0; i<5; i++)
      if(vowels[i] == x)
         return false;
   return true;
}

long long f(const string& str, int n)
{
   long long r = 0;
   for(int i=str.size()-1, c=0, l=-1; i>=0; i--)
   {
      if(cons(str[i]))
         c++;
      else
         c = 0;
      if(c >= n)
         l = i;
      if(l != -1)
         r += str.size() - l - n + 1;
   }
   return r;
}

int main()
{
   int nbTests;
   cin >> nbTests;
   for(int test=1; test<=nbTests; test++)
   {
      string str;
      int n;
      cin >> str >> n;
      cout << "Case #" << test << ": " << f(str, n) << "\n";
   }
   return 0;
}