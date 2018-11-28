// Monjurul Huda Munna
// Daffodil International University

#include <string>
#include <cstring>
#include <cmath>
#include <map>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <list>
#include <set>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

typedef long long int lld;

#define Max 10000009


int main(){

    #ifdef munnapagol
    freopen("input.txt", "r", stdin);
    freopen("vomit.txt", "w", stdout);
    #endif


    int i, j, k, h, test, kase = 0;
    int x, r, c;
    cin >> test;
    while(test--){
        cin >> x >> r >> c;
        int tot = r * c;

        int small, big;
        small = min(r,c);
        big = max(r,c);

        if(x==4 && tot%x==0 && ((r==3 && c==4) || (r==4 && c==3) || (r==4 && c==4))) cout << "Case #" << ++kase << ": GABRIEL" << endl;
        else if(x==3 && tot%x==0 && ((r==2 && c==3) || (r==3 && c==2) || (r==3 && c==3) || (r==3 && c==4) || (r==4 && c==3))) cout << "Case #" << ++kase << ": GABRIEL" << endl;
        else if( (x==2 && tot%x==0 && tot>=x) || x==1 ) cout << "Case #" << ++kase << ": GABRIEL" << endl;
        else cout << "Case #" << ++kase << ": RICHARD" << endl;

    }



    return 0;
}

