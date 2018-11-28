/**
 * Md Imran Hasan Hira (imranhasanhira@gmail.com)
 */

#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
#define MP(x,y) make_pair(x,y)

int T, x, r,c;

bool gadharKhatuni(){
    if(x==1) return false;
    if(x==2) return !(r%2==0 || c%2==0);
    if(x==3) return !(r*c==6 || r*c==9 || r*c==12 );
    if(x==4) return !(r*c==12 || r*c==16);
}


int main(){
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    cin >> T;
    for(int test=0;test<T;test++){
        cin >> x >> r >> c;
        bool r = gadharKhatuni();
        printf("Case #%d: %s\n", test+1, (r ? "RICHARD" : "GABRIEL"));
    }

    return 0;
}
