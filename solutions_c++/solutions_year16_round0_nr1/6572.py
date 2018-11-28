#include<bits/stdc++.h>
#define MI 100000000000000000
using namespace std;
long long hsh[12];
int main()
{
//    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long i,j,k,T,n,t;
    scanf("%lld",&T);
    for(t=1;t<=T;t++)
    {
        k=0;
        memset(hsh,0,sizeof hsh);
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n",t);
            continue;
        }
        i=n;
        while(i<MI)
        {
            j=i;
            while(j>0)
            {
                if(hsh[j%10]==0)
                    hsh[j%10]=1,k++;
                j/=10;
            }
            if(k==10)
            {
                break;
            }
            i+=n;
        }
        if(i>=MI)
        {
            printf("Case #%lld: INSOMNIA\n",t);
            return 0;
        }
        else
            printf("Case #%lld: %lld\n",t,i);
    }
}
