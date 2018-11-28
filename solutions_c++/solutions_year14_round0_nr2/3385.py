#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    double C,F,X,T;
    freopen("inp.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> t;
    for ( int l = 1; l <= t; l++ ) {
        cin >> C >> F >> X;
        double ans = 0.0;
        T = 2.0;
        if ( X <= C ) {
             ans = (double)X/(double)T;
        }
        else {
             while ( 1 ) {
                   ans += (double)C/(double)T;
                   double val1,val2;
                   val1 = (double)(X-C)/(double)T;
                   val2 = (double)X/(double)(T+F);
                   if ( val1 > val2 ) {  
                      T += F;
                   }
                   else {
                       ans += val1; 
                       break;
                   }    
             }
        }
        cout << "Case #" << l << ": ";
        printf("%0.7lf\n", ans);
    }
    return 0;
}
