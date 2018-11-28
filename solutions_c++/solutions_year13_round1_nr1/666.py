#include <stdio.h>
#include <stdlib.h>

    
    int T;
    long long r,t;
long long cal(long long ans){
    return (2*ans + 2*r - 3)*ans;
}

long long bis(){
    long long min = 0;
    long long max = 1,mid;
    long long tt = cal(max);
    while (tt <= t) {
        min = max+1;
        max *= 2;
        tt = cal(max);
    }
    max--;
    while (min <= max) {
        mid = (min + max) / 2;
        if (cal(mid) > t) {
            max = mid - 1;
        } else {
            min = mid + 1;
        }
    }
    return max;
}

int main(){
    freopen("a1.in","r",stdin);
    freopen("a1.out","w",stdout);
    scanf("%d",&T);
    for (int tt= 1 ; tt <= T ; tt++){
        scanf("%lld %lld",&r,&t);
        r++;
        printf("Case #%d: %lld\n",tt,bis());
    }
}
