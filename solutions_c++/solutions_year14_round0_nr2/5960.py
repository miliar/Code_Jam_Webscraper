#include<bits/stdc++.h>

using namespace std;

#define sc scanf
#define pf printf


int main()
{

     long T, kase=1;
     double C, F, X, time, xtra, miN;


     freopen("B-large.in","r", stdin);
     freopen("B_large_out.txt", "w", stdout);

     cin>>T;
     while(T--)
     {
          double cokki = 2;
          time =0;

          cin>>C>>F>>X;

          while(true)
          {
               double tt = C/cokki + X/(cokki+F);
               double tm = X/cokki;

               if(tm <= tt)
               {
                    time += tm;
                    break;
               }
               time += C/cokki;
               cokki += F;
          }
          printf("Case #%ld: %.7lf\n", kase++, time);
     }

     return 0;
}

