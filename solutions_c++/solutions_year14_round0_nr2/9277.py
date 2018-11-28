#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

double c,f,x;

int main() {
        freopen("sw.in","r",stdin);
        freopen("sw.out","w",stdout);

        int t,ca = 1;
        scanf("%d",&t);
        while(t--) {
                scanf("%lf%lf%lf",&c,&f,&x);
                double now;
                double next,per = 2,sum = 0;
                now = (x / per);
                next = (c / per + x / (per + f));
                sum += c / per;
                while(next <= now) {
                        per += f;
                        now = next;
                        next = (sum + (c / per) + x / (per + f));
                        sum += c / per;
                }

                printf("Case #%d: %f\n",ca++,now);

        }
        return 0;

}
