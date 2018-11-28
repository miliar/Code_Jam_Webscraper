#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt", "w", stdout);


    long long n, t, c =1, p;

    cin>>n;

    while(n--)
    {
        cin>>t;
        int ar [12]= {0};
        int c2 = 0, f =1, d;
        if(t==0)
        {
            printf("Case #%lld: INSOMNIA\n",c++);
            continue;
        }
        while(c2!=10)
        {
            p = t*f;
            d = p;
            while(d>0)
            {
                ar[d%10]++;
                if(ar[d%10]==1)
                    c2++;
                d = d/10;
            }

            f++;



        }
        printf("Case #%lld: %lld\n",c++,p);
    }

    return 0;

}
