// Anve$hi $hukla
#include <bits/stdc++.h>
using namespace std;
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(NULL);}}$;

typedef long long LL;
const int Maxn = 200005;
long long Val = (1LL<<10) - 1;

int main(){
   int t;
   long long n;
   cin >> t;
   string s = "INSOMNIA";
   for(int x=1;x<=t;x++){
      cin >> n;
      if(n == 0){
         //case(x, s);
         cout << "Case #" << x << ": " << s << endl;
      }

      else{
         long long temp = n;
         long long Cur = 0;
         for(int i=1;i<1000000;i++){
            long long temp1 = 1LL * temp * i;
            while(temp1){
               int x = temp1%10;
               temp1 /= 10;
               Cur |= (1LL<<x);
            }
            if(Cur == Val){
               temp1 = 1LL * temp * i;
               //case(x, temp1);
               cout << "Case #" << x << ": " << temp1 << endl;
               break;
            }
         } 
      }
   }
   return 0;
}
