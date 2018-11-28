#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define PI (3.141592653589793)
#define epsilon (1e-12)
#define MAX (((long long int) 1) << 30)

void solve(){

    long long int r,t;
    long long int up = MAX , low = 1;
    cin >> r >> t;
    //cout << "bliaaaA";
    fflush(stdout);
    /*
    long long int best = 0;
    while ( low <= up ){
        long long int med = (low+up)/2;
        if ( PI * ( (2*r+1)*med + 2*med*(med-1) ) <= t)
        {
            best = max(med,best);
            low = med +1;
        }
        else 
            up = med-1;
    }
    */
    long long int T = 0;
    long long int sum = ( 2*r + 1 );
    while ( sum <= t  ) 
    {
        T++;
        sum += (2*r +1 + 4*T);
    }
    cout << T << '\n';
};

int main(){
    int t;
    cin >> t;
    for (int i=1;i<=t;i++)
    {
        cout << "Case #" << i << ": " ;
        solve();
    }
    return 0;
}
