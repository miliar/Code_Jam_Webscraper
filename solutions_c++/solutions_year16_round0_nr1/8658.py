#include <iostream>
#include <set>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);

    int t,count=1;
    long long int n,tmp,inc;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld",&n);
        set<int> myset;
        inc=n;
        while(myset.size()!=10)
        {
            if(n==0)
                break;
            tmp=n;
            while(tmp>0)
            {
                myset.insert(tmp%10);
                tmp=tmp/10;
                if(myset.size()==10)
                    break;
            }
            //if(myset.size()==10)
              //      break;
            n=n+inc;
        }

        printf("Case #%d: ",count++);
        if(n==0)
            printf("INSOMNIA\n");
        else
            printf("%lld\n",n-inc);
    }

    return 0;
}
