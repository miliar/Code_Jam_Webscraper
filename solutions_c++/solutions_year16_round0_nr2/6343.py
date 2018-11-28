#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
char str[200];
int main()
{
   int kase;
   int t;
   int n;
   int diff;
   int i;
   cin >> t;
   for(kase=1;kase<=t;kase++) {
       diff = 0; 
       cin >> str;
       int len = strlen(str);

       for(i=0;i<len-1;i++) {
           if(str[i] != str[i+1])
               diff++;
       }
       if (str[len-1] == '-' )
           diff++;

       cout << "Case #"<<kase<<": ";
       cout << diff << endl;
   }
   return 0;
}
