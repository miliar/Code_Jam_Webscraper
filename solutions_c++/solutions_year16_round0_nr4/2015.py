#include<cstdio>
#include<cstring>

int main () {
freopen("D-large.in","r",stdin);
freopen("out.txt","w",stdout);
    long long t,tt,k,c,s,i;
    scanf("%I64d",&tt);
    for (t=1;t<=tt;t++) {
        scanf("%I64d%I64d%I64d",&k,&c,&s);
        if (s*c<k) {
            printf("Case #%I64d: IMPOSSIBLE\n",t);
            continue;
        }

        printf("Case #%I64d: ",t);
        long long ans=1,temp=1;
        for (i=0;i<k;i++) {
            ans+=i*temp;
            temp*=k;
            if (i % c==c-1) {
                printf("%I64d ",ans);
                ans=1;
                temp=1;
            }
        }

        ans=1;
        temp=1;
        if (k % c != 0) {
            long long sk=k-(k%c);
            for (i=k-1;i>=sk;i--){
                ans+=i*temp;
                temp*=k;
            }
            printf("%I64d ",ans);
        }

        puts("");
    }
    return 0;
}
