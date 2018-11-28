#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

unsigned long long rev(unsigned long long n){
    unsigned long long r=0;
    for(unsigned long long m=10; m/10 <= n; m*=10)
        r = r*10 + (n%m)/(m/10);
    return r;
}

int main(){
    int t;
    cin >> t;
    for(int tc=1; tc<=t; ++tc){
        unsigned long long n;
        cin >> n;
        vector<unsigned long long> c(n+1, n+1);
        c[1] = 1;
        vector<unsigned long long> p(n+1, 0);
        for(unsigned long long i=1; i<n; ++i){
            if(c[i+1] > c[i]+1){
                c[i+1] = c[i]+1;
                p[i+1] = i;
            }
            unsigned long long rv = rev(i);
            if(rv <= n && c[rv] > c[i]+1){
                assert(rv > i);
                c[rv] = c[i]+1;
                p[rv] = i;
           }
        }
        cout << "Case #" << tc << ": " << c[n] << endl;
    }
    return 0;
}
