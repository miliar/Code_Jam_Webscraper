#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <cstdio>
#define ll long long int
#define floop(n,m) for(int i=(int)n ; i<(int)m ; i++)
using namespace std;

vector <bool> isPrime ;
vector <int> primes ;



int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t ;
    for(int j=1 ; j<=t ; j++){
        int max_s;
        cin >> max_s ;
        int total = 0;
        string s;
        cin >> s;
        total = 0;
        total += (int)(s.at(0)-'0');
        int ans = 0;
        for(int i=1 ; i<max_s+1 ; i++){
            int x = (int)(s.at(i)-'0');
            if(total < i && x>0){
                ans += i-total ;
                total += ans ;
            }
            total += x;
        }
        cout << "Case #" << j <<": "<<ans << endl ;
    }
    return 0;
}
