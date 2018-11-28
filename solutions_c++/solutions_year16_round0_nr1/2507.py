#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
   int T;
   scanf("%d", &T);
   for(int _t=1; _t<=T; _t++){
      int n;
      scanf("%d", &n);
      if(n == 0) {
         printf("Case #%d: INSOMNIA\n", _t);
         continue;
      }
      int nDig = 0;
      bool dig[10] = {false};
      int k = 0;
      while(nDig < 10) {
         k += n;
         int l = k;
         while(l > 0) {
            int d = l % 10;
            if(!dig[d]){
               nDig++;
               dig[d] = true;
            }
            l /= 10;
         }
      }
      printf("Case #%d: %d\n",_t, k);
   }
   return 0;
}
