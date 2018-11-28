#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

int a[12];

int pan()
{
    for (int i=0;i<10;i++)
    if (a[i]==0) return 0;
    return 1;
}

int main()
{
    int T;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for (int _=1;_<=T;_++){
        int n;
        cin>>n;
        memset(a,0,sizeof(a));
        int ans=-1;
        for (int j=1;j<=123456;j++)
        {
            ll tmp=(ll) j*n;
            while (tmp)

            {
                a[tmp%10]++;
                tmp/=10;
            }
           if (pan())
           {
               ans=j*n;
               break;
           }
        }

        if (ans==-1)  printf("Case #%d: INSOMNIA\n",_);
        else printf("Case #%d: %d\n",_,ans);
        }


    return 0;
}
