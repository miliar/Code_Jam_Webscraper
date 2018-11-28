#include <iostream>
#include <stdio.h>
#include <string.h>
#include <set>

using namespace std;
int a[11];

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    int t,ca;
    long long n,m;
    scanf("%d",&t);
    for(int ca = 1;ca <= t ; ca++){
        scanf("%I64d",&n);
        m = n;
        int sum = 0;
        memset(a,0,sizeof(a));
        while(1){
            if(n == 0)
                break;
            long long p = n;
            while(p){
                if(a[p%10] == 0){
                    a[p%10] = 1;
                    sum++;
                }
                p/= 10;
            }
            if(sum == 10)
                break;
            n+=m;
        }
        printf("Case #%d: ",ca);
        if(sum == 10)
        printf("%I64d\n",n);
        else printf("INSOMNIA\n");
    }
    return 0;
}
