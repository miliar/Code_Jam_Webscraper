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
   int xx;
   for (int i = 0; i <= 1000; i++) a[i] = 0;
   int ans = 0; int max;
   for (int i = 0; i < num; i++)
   {
      cin >> xx;
      if (ans < xx) ans = xx;
      a[xx]++;
   }
   max = ans;
   for (int i = 1; i< max; i++)
   {
       int h; h = 0;
       for (int j = i+1; j <= max; j++)
       {
         int tmp = j/i - 1;
         if (j%i != 0) tmp++;
         h = h+a[j]*tmp;
       }
       if (ans > h+i) ans = h+i;
         
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
  
