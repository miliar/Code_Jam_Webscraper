#include<cstdio>
long long a,b,k,ac,T;
int main(){
    scanf("%I64d",&T);
    for (int o=1; o<=T; o++){
        scanf("%I64d%I64d%I64d",&a,&b,&k);
        ac=0;
        for (long long i=0; i<a; i++)
            for (long long j=0; j<b; j++)
                if ((i&j)<k) ++ac;
        printf("Case #%d: %I64d\n",o,ac);
    }
    return 0;    
}
