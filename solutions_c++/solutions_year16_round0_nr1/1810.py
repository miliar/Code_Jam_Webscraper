#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll n, k, i, j, l, t=1, a[10], flag, ans[105];
    cin>>t;
    for(l=1; l<=t; l++)
    {
        cin>>n;
        if(n==0)
        {
            ans[l]=-1;
            continue;
        }
        for(i=0; i<10; i++)
            a[i]=0;
        flag=i=0;
        while(!flag)
        {
            i++;
            k=i*n;
            while(k)
            {
                a[k%10]=1;
                k/=10;
            }
            flag=1;
            for(j=0; j<10; j++)
                if(!a[j])
                    flag=0;
        }
        ans[l]=i*n;
    }
    for(l=1; l<=t; l++)
    {
        cout<<"Case #"<<l<<": ";
        if(ans[l]==-1)
            cout<<"INSOMNIA\n";
        else
            cout<<ans[l]<<endl;
    }
    return 0;
}
