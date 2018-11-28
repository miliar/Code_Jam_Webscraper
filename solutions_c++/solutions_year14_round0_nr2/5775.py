#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<cmath>

typedef long long ll;

using namespace std;

int main(){
    freopen("input.in","r",stdin);
    freopen("output.out","w", stdout);

    int t;
    int ntc = 1;
    cin >> t;
    double C,F,X;
    while( t-- ){
        cin >> C >> F >> X ;
        double ans = 9999999999.9;
        double last = ans;
        double cant = 0;
        double accum = 0.0;


        while( true ){
            double cur = accum + X/( 2+ cant *F );

            accum += C/( 2+ cant *F );
            cant += 1.0;

            ans = min( ans, cur );
            if( cur > ans )
                break;

        }

        printf("Case #%d: ", ntc);
        printf("%.9f\n",ans );
        ntc++;

    }

    return 0;
}
