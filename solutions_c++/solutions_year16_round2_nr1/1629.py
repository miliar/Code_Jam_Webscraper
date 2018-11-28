#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

const int S = 2000;

const string t[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
const int u[] = {0, 6, 2, 7, 5, 4, 1, 9, 8, 3};
const string x = "ZXWSVFONIT";

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      string s;
      cin >> s;
      int o[100] = {0};
      for(char c : s)
         o[c]++;
      int r[10] = {0};
      for(int i=0; i<10; i++)
      {
         int j = u[i];
         char c = x[i];
         while(o[c])
         {
            for(char a : t[j])
               o[a]--;
            r[j]++;
         }
      }
      cout << "Case #" << test << ": ";
      for(int i=0; i<10; i++)
         while(r[i]--)
            cout << i;
      cout << endl;
   }
   return 0;
}