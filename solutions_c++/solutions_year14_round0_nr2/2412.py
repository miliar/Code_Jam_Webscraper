/* In the name of ALLAH, most gracious, most merciful */

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cassert>
#include <set>
#include <ctime>
#include <iomanip>
#include <cstring>
#include <map>
 
using namespace std;
typedef long long ll;
typedef pair< int, int > pi;

const int MAXI = 50000;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
#endif
    int t = 1, T;
    cin >> T;
    while(T--){
        long double C, F, X;
        cin >> C >> F >> X;

        long double besti = X / 2; 
        long double prev = C / 2.0, cookiesPs = 2.0;
        for(int i = 1; i <= MAXI; i++){
            cookiesPs += F;
            besti = min(besti, prev + (X / cookiesPs));
            prev += C / cookiesPs;
            if(prev > besti) break;
        }

        cout << "Case #" << t++ <<  ": ";
        cout << setprecision(8) << besti << endl;
    }
    
    return 0;
}