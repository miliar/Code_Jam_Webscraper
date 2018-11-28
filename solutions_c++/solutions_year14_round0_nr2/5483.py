#include <cstdio>

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;
    double c, f, x, total, per, time;
    scanf("%d",&T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        time = 0.0;
        total = x / 2.0;
        per = 2.0;
        while(true)
        {
            time += c / per;
            per += f;
            if(total < time + x / per)
                break;
            else
                total = time + x / per;
        }
        printf("Case #%d: %.7lf\n", t, total);
    }
    return 0;
}
