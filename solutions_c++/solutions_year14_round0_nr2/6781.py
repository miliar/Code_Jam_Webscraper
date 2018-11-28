#include<cstdio>

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int cas,t=0;
    double c,f,x,ans,d,cur;
    scanf("%d",&cas);
    while(cas--){
        scanf("%lf%lf%lf",&c,&f,&x);
        ans = x/d;
        cur = 0;
        d = 2;
        while( (c/d+x/(d+f) < x/d) ){
            cur += c/d;
            d += f;
        }
        ans = cur + x/d;
        printf("Case #%d: %.8lf\n",++t,ans);
    }
    return 0;
}
