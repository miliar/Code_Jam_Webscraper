#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int T=1;T<=t;T++) {
        double c , f , x;
        cin >> c >> f >> x;
        double pre = 2.0 , ans = 0.0;
        if(x < c) ans = x/pre;
        else {
            while(x/(pre+f) < (x-c)/pre) {
                ans += c/pre;
                pre += f;
            }
            ans += x/pre;
        }
        printf("Case #%d: %0.7lf\n",T,ans);
    }
    return 0;
}
