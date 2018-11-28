#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    long long r;
    long long b;
   // double pi=3.1415926535897932;
    long long s=3;
    for (int o_O=0;o_O<t;o_O++){
          cout << "Case #" << o_O+1 << ": ";
          cin >> r >> b;
          long long ans=1;
          while ((2*r+2*ans-1)*ans <= b){
            ans++;
          }
          ans--;
          cout << ans << endl;
    }
    return 0;
}
