#include <bits/stdc++.h>

using namespace std;

int tc;
double c,f,x,pr,ans;
const double eps=1e-9;

int main(){
    freopen("a.inp","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&tc);
    for(int tt=1;tt<=tc;++tt){
        scanf("%lf%lf%lf",&c,&f,&x);
        pr=2.0;
        ans=0.0;;
        while (1){
            if ( c/pr+x/(pr+f) <x/pr ){
                ans+=(c/pr);
                pr+=f;
            }else{
                ans+=(x/pr);
                break;
            }
        }
        printf("Case #%d: %.17lf\n",tt,ans);
    }
    return 0;
}
