#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;

double work(double c,double f,double x) {
        int lim = int((f*x-c*f-2*c)/(f*c));
        if (lim<0) lim = 0;
        double cur = 0,ret = x/2;
        for (int i = 0; i < lim+20; i ++) {
                cur += c/(i*f+2);
                ret = min(ret,cur+x/(i*f+f+2));
        }
        return ret;
}

int main() {
        int cas,ca = 0;
        double c,f,x;
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
        scanf("%d",&cas);
        while (cas--) {
                scanf("%lf%lf%lf",&c,&f,&x);
                printf("Case #%d: %.7f\n",++ca,work(c,f,x));
        }
        return 0;
}
