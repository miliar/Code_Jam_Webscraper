#include <iostream>
#include <cstdio>
#include <algorithm>
#include <math.h>
using namespace std;
int mass1[4][4], mass2[4][4];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    for(int test = 1; test <= n; test++){
        double  c,f,x;
        cin >> c>>f>>x;
        double t = 0;
        double ans = 1000000000;
        for(int i = 0; i < 50001; i++){
            ans = min(ans,t+(x/(2+i*f)));
            t += c/(2+i*f);
        }
        printf("Case #%d: %.7lf\n",test,ans);
    }
    return 0;
}
