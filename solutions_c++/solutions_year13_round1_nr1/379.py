#include <iostream>
#include <cmath>
using namespace std;

long long t,r;
int tn,tt;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("pA_large.out","w",stdout);
    
    cin >> tn;
    for (tt=1;tt<=tn;tt++)
    {
        cin >> r >> t;
        /*long double ddelta = ((long double)(2*r-1)*(long double)(2*r-1)+(long double)8*t);
        long double delta = sqrt(ddelta);
        long double ans = (long double)(1-2*r + delta)/4.0;
        long long n = (long long)ans;*/
        long long ll=0, rr=t;
        while (ll+1<rr)
        {
              long long mid = (ll+rr)/2;
              if (sqrt(t) < sqrt(2)*mid)
              {
                  rr = mid;
                  continue;
              }
              if ((double)t/(2*r-1) < mid)
              {
                  rr = mid;
                  continue;
              }
              if (2*mid*mid + (2*r-1)*mid <= t)
              {
                  ll =  mid;
                  continue;
              }
              else
              {
                  rr = mid;
                  continue;
              }
        }
        long long n = ll;
        
        cout << "Case #" << tt << ": " << n << endl;        
    }
}
