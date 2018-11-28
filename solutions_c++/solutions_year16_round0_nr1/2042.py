#include<cstdio>
#include<cstring>

int main () {
//freopen("A-large.in","r",stdin);
//freopen("out.txt","w",stdout);
    int t,tt,n,i,g;
    long long s;
    scanf("%d",&tt);
    for (t=1;t<=tt;t++) {
        scanf("%d",&n);
        if (n==0) {
            printf("Case #%d: INSOMNIA\n",t);
            continue;
        }
        g=0;
        s=n;
        int mid=s;
        while (mid>0) {
            g|=(1 << (mid % 10));
            mid /= 10;
        }
        //printf("%d\n",g);
        while (g!=(1 << 10) - 1) {
            s+=n;
            int mid=s;
            while (mid>0) {
                g|=(1 << (mid % 10));
                mid /= 10;
            }
        }
        printf("Case #%d: %I64d\n",t,s);
    }
    return 0;
}
