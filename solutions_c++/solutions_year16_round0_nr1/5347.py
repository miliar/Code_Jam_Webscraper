#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[]) {
    int test,ti=0;
    long long int i,k;
    long long int n,m;
    scanf("%d",&test);
    while(test--)
    {
        ti++;
        scanf("%lld",&n);
        printf("Case #%d: ",ti);
        if(n==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int bit=0,j;
        i=1;
        while(bit!=1023)
        {
            m=n*i;
            i++;
            while(m)
            {
                j=m%10;
                m/=10;
                bit=bit|(1<<j);
            }
        }
        printf("%lld\n",n*(i-1));
    }
    return 0;
}
