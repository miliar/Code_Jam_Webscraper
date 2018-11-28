#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
#define MIN(x,y) (x<y?x:y)

int main(){
    int T;
    int Case = 0;
    freopen("in.txt", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    while(T--){
        double C,F,X;
        int k;
        double ans;

        scanf("%lf%lf%lf", &C, &F, &X);
        k = (int)ceil((F*X-2*C-F*C)/(F*C*1.0));
        ans = 0;
        for(int i=0; i<k; ++i){
            ans += (1.0*C)/(2+i*F);
        }
        if(k>0)
            ans += (1.0*X)/(2+k*F);
        else
            ans = (1.0*X)/2;
        printf("Case #%d: %.7lf\n", ++Case, ans);
    }
    return 0;
}
