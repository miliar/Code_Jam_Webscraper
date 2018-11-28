#include<bits/stdc++.h>
using namespace std;
#define LLT long long int

LLT a[11];

int isprime(LLT n)
{
    int ffff = 0;
    for(LLT i=2; i*i<=n; ++i) {
        if(n%i==0) {
            ffff = 1;
            break;
        }
    }
    return ffff;
}

LLT powerbi(LLT a, LLT b)
{
    if(b==0) return 1;
    LLT temporary = powerbi(a,b/2);
    if(b%2==0) return temporary*temporary;
    else
        return a*temporary*temporary;
}



int main()
{
    LLT t,i,j,n,k;
    scanf("%lld", &t);
    for(LLT ii=1; ii<=t; ii++) {
        scanf("%lld %lld", &n, &j);
        int fl = 0;
        LLT jj=0;
        printf("Case #%lld:\n", ii);
        for(i=0; i<(1<<(n-2)) && jj<j; i++) {
            fl=0;
            for(LLT p=2; p<=10; p++) {
                a[p] = 1 + powerbi(p,n-1);
            }
            for( k=0; k<n-2; k++) {

                LLT y = 1<<k;

                if(i&y) {
                    for(LLT l=2; l<=10; l++) {
                        a[l] = a[l] + powerbi(l,k+1);
                    }
                }
            }

            for(LLT q=2; q<=10; q++) {
                if(!isprime(a[q])) {
                    fl = 1;
                    break;
                }
            }
            if(fl==0) {
                jj++;
                printf("%lld ", a[10]);
                for(LLT q=2; q<=10; q++) {
                    for(LLT r=2; r*r<=a[q]; r++) {
                        if(a[q]%r==0) {
                            printf("%lld ",r);
                            break;
                        }
                    }
                }
                printf("\n");
            }
        }
    }
    return 0;
}
