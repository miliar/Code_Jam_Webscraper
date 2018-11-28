#include<bits/stdc++.h>
using namespace std;


int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("outA.txt", "w", stdout);

    int t, n, tc,i,p,k, tm;
    int ara[15];

    cin>> t;
    for(tc=1; tc<=t; tc++)
    {
        cin>>n;
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n", tc);
            continue;
        }
        for(i=0; i<=9; i++)
        {
            ara[i]=0;
        }
        bool f=0;
        int cnt=0;
        for(i=1; ;i++)
        {
            k= i*n;
            tm=k;
            while(k>0)
            {
                p= k%10;
                k/=10;
                if(ara[p]==0)
                {
                    ara[p]=1;
                    cnt++;
                }
            }
            if(cnt>9) break;
        }
        printf("Case #%d: %d\n",tc,tm);
    }
    return 0;
}
