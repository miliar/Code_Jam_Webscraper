#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    //freopen("D-small-attempt0.in","r",stdin);
    //freopen("D-small.out","w",stdout);
    freopen("D-large.in","r",stdin);
    freopen("D-Large.out","w",stdout);
    int t, T, X, R, C, W, ans;
    scanf("%d",&T);
    for ( t = 1 ; t <= T ; t ++ ) {

        scanf("%d %d %d",&X,&R,&C);
        if ( C > R )
            swap(R,C);

        W = (X+1)/2; // 最大寬度
        if ( X >= 7 ) ans = 0; // R 選有空洞的必勝
        else if ( R >= X && C >= W ) { // 確保 R 不管選哪種omino 至少不會放不進去 ( 階梯跟1直線 )
            if ( (R*C)%X != 0 ) ans = 0; // 面積不合法, R必勝
            else if ( C == W && X > 3 ) {// 截斷的情況且X > 3 ( 階梯 )
                if ( X == 4 ) ans = 0;
                else if ( X == 5 ) {
                    if ( R >= 10 ) ans = 1;
                    else ans = 0;
                }
                else ans = 0; // X == 6
            }
            else ans = 1;
        }
        else ans = 0;

        printf("Case #%d: %s\n",t,ans==0?"RICHARD":"GABRIEL");
    }

    return 0;
}
