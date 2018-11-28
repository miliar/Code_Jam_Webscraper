#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n;
    cin>>n;
    for(int t=1;t<=n;t++)
    {
        ll x,cnt=1,ans=10;
        cin>>x;
        if(x==0)
        {
            cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        bool f[10];
        for(int i=0;i<10;i++)
            f[i]=0;
        while(ans)
        {
            ll tmp=x*cnt;
            while(tmp)
            {
                if(f[tmp%10]==0)
                    ans--;
                f[tmp%10]=1;
                tmp/=10;
            }
            cnt++;
        }
        cnt--;
        cout<<"Case #"<<t<<": "<<x*cnt<<endl;
    }
}
