#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int main()
{
   int T;
   scanf("%d", &T);
   char s[101];
   for(int _t=1; _t<=T; _t++){
      scanf("%s", s);
      int n = strlen(s);
      int k = 0;
      for(int i=1; i<n; i++)
         if(s[i] != s[i-1])
            k++;
      if(s[n-1] == '-')
         k++;

      printf("Case #%d: %d\n",_t, k);
   }
   return 0;
}
