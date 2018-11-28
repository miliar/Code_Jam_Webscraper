#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<vector>
#include<map>
#define MAX 10000000L * 10000000L
using namespace std;
long long fairSquarePalin[10000000];
map<long long, bool> isFairSquarePalin;
bool isPalin(long long x) {
    long long rev = 0, original = x;
    while(x) {
        rev = rev * 10 + x % 10;
        x /= 10;
    }
    return original == rev;
}
int main() {
    fairSquarePalin[0] = -1;
    long long len = 1;
    for(long long i = 1 ; i*i <= MAX ; i++) {
        if( isPalin(i) && isPalin(i*i) ) {
            fairSquarePalin[len++] = i*i;
            isFairSquarePalin[ i*i ] = 1;
        }
    }
    int t;
    cin >> t;
    for(int Kases = 1 ; Kases <= t ; Kases++) {
        cout<<"Case #" << Kases << ": ";
        long long min, max;
        cin>>min>>max;
        --min;
        long long upper = upper_bound(fairSquarePalin, fairSquarePalin + len, max) - fairSquarePalin - 1;
        long long lower = lower_bound(fairSquarePalin, fairSquarePalin + len, min) - fairSquarePalin - !isFairSquarePalin[min];
        cout << upper - lower << "\n";
    }
    return 0;
}
