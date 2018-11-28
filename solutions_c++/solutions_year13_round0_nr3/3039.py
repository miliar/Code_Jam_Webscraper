#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;

typedef long long LL;

LL T,n,m,a,b;

bool check(LL a)
{
    LL b=0,temp=a;
    while(a)
    {
        b*=10;
        b+=a%10;
        a/=10;
    }
    return b==temp;
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    cin>>T;
    int cs=0;
    while (T--)
    {
        cs++;
        LL ans=0;
        cin>>a>>b;
        int sa=sqrt(a);
        if (sa*sa<a) sa++;
        int sb=sqrt(b);
        for (int i=sa; i<=sb; i++)
        {
            if (check(i))
            {
                LL ns=i*i;
                if (check(ns))
                    ans++;
            }

        }
        printf("Case #%d: ",cs);
        cout<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
