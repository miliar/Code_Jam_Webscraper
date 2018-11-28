#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int map[10];
long noMap, n;

void putMap(long n) {
    while(n != 0) {
        if(map[n%10] == 0) {
            map[n%10] = 1; noMap++;
        }
        n /= 10;
    }
}

long process() {
    if( n== 0 ) return 0;
    int i = 0;
    for(i=0;i<10;i++) map[i] = 0;
    noMap = 0;
    for(i=1;;i++) {
        putMap(n*i);
        if(noMap == 10) break;
    }
    return n*i;
}

int main() {
    int t;
    cin>>t;
    for(int i=1;i<=t;i++) {
        cin>>n;
        long ans = process();
        cout<<"Case #"<<i<<": ";
        if(ans == 0) cout<<"INSOMNIA"<<endl;
        else cout<<ans<<endl;
    }
    return 0;
}