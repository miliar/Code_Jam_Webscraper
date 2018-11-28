#include <iostream>
#include <algorithm>
#include <inttypes.h>

using namespace std;

int n;

int solve(int c, uint16_t seen) {
    for(int i = c; i>0; i=i/10)
        seen = seen | (1<<(i%10));
    if(seen==1023)
        return c;

    return solve(c+n, seen);
}

int main() {
    int t;
    cin>>t;
    for(int i = 0; i<t; i++) {
        cin>>n;
        if(n==0)
            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<solve(n,0)<<endl;
    }
}
