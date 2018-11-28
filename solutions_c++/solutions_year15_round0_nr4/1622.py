#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <map>
#include <utility>
#include <set>
#include <memory>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

using namespace std;

#define GAB "GABRIEL"
#define RIC "RICHARD"
int T;
int X, R, C;

string solve(){
    int s = min(R,C);
    int l = max(R,C);
    if (X==1) return GAB;
    if (X==2) {
        if (s==1 && l==1) return RIC;
        if (s==1 && l==3) return RIC;
        if (s==3 && l==3) return RIC;
        return GAB;
    }
    if (X==3) {
        if (s==2 && l==3) return GAB;
        if (s==3 && l==4) return GAB;
        if (s==3 && l==3) return GAB;
        return RIC;
    }
    if (s==4 && l==4) return GAB;
    if (s==3 && l==4) return GAB;
    return RIC;
}

int main(int argc, char *argv[]) {
    cin>>T;
    for(int t=1;t<=T;++t) {
        cin >> X >> R >> C;
        cout<<"Case #"<<t<<": "<<solve()<<endl;
    }
    return 0;
}
