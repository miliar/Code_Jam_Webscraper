#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#define MAX 1005

int main(){
    #ifndef ONLINE_JUDGE
     freopen("D-small-attempt0.in","r",stdin);
     freopen("output.out","w",stdout);
    #endif // ONLINE_JUDGE
   char a[MAX];
   int T;
   scanf("%d",&T);
    for(int i= 1; i<= T; i++){
        int x, r, c;
        scanf("%d%d%d", &x, &r, &c);
        bool ok = true;
        if (x == 1) ok = false;
        if (x == 2 && (r%2==0 || c%2==0)) ok = false;
        if (x == 3 && ((r == 3 && c >= 2) || (c == 3 && r >=2))) ok = false;
        if (x == 4 && ((r == 4 && c >= 3) || (c == 4 && r >=3))) ok = false;
        if (ok) printf("Case #%d: RICHARD\n", i);
        else printf("Case #%d: GABRIEL\n", i);
    }
    return 0;
}
