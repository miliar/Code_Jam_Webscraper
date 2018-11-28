#include <iostream>
#include <cstdio>

using namespace std;

int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int _T;
    scanf("%d", &_T);
    for (int T = 1; T <= _T; T++){
        int S, ans = 0, tmp = 0;
        char c;
        scanf("%d", &S);
        for (int i = 0; i <= S; i++){
            scanf(" %c", &c); c-='0';
            //~ cerr<<i<<","<<(int)c<<","<<tmp<<","<<ans<<endl;
            if (tmp >= i)
                tmp += c;
            else {
                ans += i-tmp;
                tmp += c + (i-tmp);
            }
        }
        printf("Case #%d: %d\n", T, ans);
    }
    return 0;
}
