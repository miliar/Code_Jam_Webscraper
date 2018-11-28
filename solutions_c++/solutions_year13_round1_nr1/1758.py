#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iomanip>
#include <list>

using namespace std;
#define deb(a) cout<<#a<<":"<<a<<endl;

double paint(long long r) {
    return ((r+1)*(r+1) - r*r);
}

long long calc(long long r, long long t) {
    long long res = 0;
    long long paintLeft = t;
    long long paintNeeded = paint(r);

    while(paintLeft >= paintNeeded) {
        res++;
        r+=2;
        paintLeft -= paintNeeded;
        paintNeeded = paint(r);
    }

    return res;
}

int main() {
    int T;
    cin>>T;
    
    for(int i=1; i<=T; i++) {
        long long r, t;
        cin>>r>>t;

        long long res = calc(r, t);
        cout<<"Case #"<<i<<": "<<res<<endl;
    }
    return 0;
}
