#include <cstdio>
#include <cmath>
#include <string>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

int n;
double v, x;
double r[100], c[100], vol[100];

void solve(){
    if(n == 1){
        if(c[0] == x)
            printf("%.8f\n", v/r[0]);
        else
            printf("IMPOSSIBLE\n");
    }else{
        if(c[0] == c[1] && c[0] == x)
            printf("%.8f\n", v/(r[0]+r[1]));
        else if(c[0] == x)
            printf("%.8f\n", v/r[0]);
        else if(c[1] == x)
            printf("%.8f\n", v/r[1]);
        else if((c[0] < x && c[1] < x) || (c[0] > x && c[1] > x))
            printf("IMPOSSIBLE\n");
        else{
            vol[0] = v*(x-c[1])/(c[0]-c[1]);
            vol[1] = v*(x-c[0])/(c[1]-c[0]);
            printf("%.8f\n", max(vol[0]/r[0], vol[1]/r[1]));
        }
    }
}
int main()
{
    freopen("/Users/bochen/Downloads/textfile.in","r", stdin);
    freopen("/Users/bochen/Downloads/textfile.out","w", stdout);

    int t;
    cin >> t;
    for(int cid = 1; cid <= t; cid++){
        cin >> n >> v >> x;
        for(int i = 0; i < n; i++)
            cin >> r[i] >> c[i];
        printf("Case #%d: ", cid);
        solve();
    }
    return 0;
}
