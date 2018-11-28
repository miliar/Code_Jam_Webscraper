#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <stdio.h>
using namespace std;

int a[10001];

int doit()
{
   int num;
   cin >> num;
   char ch;
   for (int i = 0; i <= num; i++)
   {
     cin >> ch;
     a[i] = ch - '0';
   }
   int ans = 0; int tmp = 0;
   for (int i = 0; i <= num; i++)
   {
     if (a[i] == 0) continue;
     if (tmp < i) { ans+= i-tmp; tmp = i;}
     tmp += a[i];
   }
   cout << ans;
   return 0;
}

int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int testcase;
  cin >> testcase;
  for (int i = 0; i < testcase; i++)
  {
    cout << "Case #" << i+1 << ": ";
    doit();
    cout << endl;
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
  
