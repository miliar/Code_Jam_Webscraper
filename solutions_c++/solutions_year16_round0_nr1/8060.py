#include <bits/stdc++.h>

using namespace std;
int main()
{
    long long int t,res,a,b,i,j,d;
    cin>>t;
    for(i=0;i<t;i++)
    {
        int c[10]={0,0,0,0,0,0,0,0,0,0};
        cin>>a;
        if(a==0)
        {
            printf("Case #%d: INSOMNIA\n",i+1);
            continue;
        }
        d=0;
        res=0;
        while(res!=10)
        {
            d=d+a;
            b=d;
            while(b!=0)
            {
                c[b%10]=1;
                b=b/10;
            }
            res=0;
            for(j=0;j<10;j++)
            {
                res = res+c[j];
            }
        }
        printf("Case #%lld: %lld\n",i+1,d);
    }

}
