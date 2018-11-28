#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cassert>

using namespace std;

int main()
{
    FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);

    long long t,n,m,d,i,j,k,ca=1,p,q,a[10];

    scanf("%lld",&t);

    while(t--){
        scanf("%lld",&n);

        for(i=0;i<10;i++){
            a[i] = 0;
        }

        if(n==0){
            printf("Case #%lld: INSOMNIA\n",ca++);
        }
        else{
            p = 0;
            k = 1;

            while(p==0){
                m = k*n;
                d = m;

                while(m!=0){
                    q = m%10;
                    m/=10;

                    a[q] = 1;
                }
                p = 1;

                for (i=0;i<10;i++){
                    if(a[i]==0){
                        p = 0;
                        break;
                    }
                }
                k++;
            }

            printf("Case #%lld: %lld\n",ca++,d);
        }
    }

    return 0;
}
