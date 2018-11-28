#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <math.h>
#include <algorithm>

using namespace std;

bool isP(int x)
{
    int div=1;
    while(x/div>=10) div*=10;
    while(x!=0) {
        int l=x/div;
        int r=x%10;
        if(l!=r) return false;
        x=(x%div)/10;
        div/=100;
    }
    return true;
}

int countP(const int& n, const int& m)
{
    int p=0;
    for(int x=n; x<=m; x++)
    {
        if(isP(x)) {
            double y = sqrt(x);
            int z = static_cast<int>(y);
            if ( fabs(y-z) < 10e-16 ) {
                if (isP(z)) {
//                    cout << x << " ";
                    p++;
                }
            }
        }
    }
//    cout << endl;
    return p;
}

int main(int argc, char * argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int TT;
    scanf("%d", &TT);
    for(int T=1;T<=TT;++T)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        int p = countP(n,m);
        printf("Case #%d: %d\n",T,p);
    }
    return 0;
}
