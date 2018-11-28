#include <iostream>
#include<bits/stdc++.h>
using namespace std;
#define int long long
int cnt[11];

int upd(int n)
{
    while(n!=0)
    {
        cnt[n%10]++;
        n/=10;
    }
}
int check()
{
    for(int i=0;i<10;i++)
        if(cnt[i]==0)
         return 0;
    return 1;
}
main()
{
    freopen("input7.txt","r",stdin);
    freopen("output7.txt","w",stdout);
    int t,n,i;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        cin>>n;
        if(n==0)
        {
            printf("Case #%lld: ",k);
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        memset(cnt,0LL,sizeof(cnt));
        i=1;
        while(1)
        {
            upd(i*n);
            if(check())
                break;
            i++;
        }
        printf("Case #%lld: ",k);
        cout<<i*n<<endl;
    }
    return 0;
}
