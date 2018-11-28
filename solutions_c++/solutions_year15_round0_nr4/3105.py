#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <limits>
#define G "GABRIEL"
#define R "RICHARD"

using namespace std;

string check(int x, int r, int c){
    if (x==1)
        return G;
    if (x> r*c)
        return R;
    if ((r*c)%x != 0)
        return R;
    if (x==2)
        return G;
    if (x==3 && (c==1 || r==1))
        return R;
    if (x==3)
        return G;
    if (r<3 || c<3)
        return R;
    return G;
}

int main(){
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);
    int T, i;
    cin >> T;
    for (i=1; i<=T; i++)
    {
        int x, c, r;
        cin >> x >> r >>c;
        cout <<"Case #" << i << ": " << check(x,r,c) <<endl;
    }
    return 0;
}
