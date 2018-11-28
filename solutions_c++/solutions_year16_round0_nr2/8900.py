#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define SF scanf
#define PF printf
#define INP          freopen("B-large.in", "r", stdin);
#define OUT          freopen("B-large.out", "w", stdout);
char st[150];
int main()
{
    int n,t,i,j,k,n1,c1,f,l;
    ll ans,m;
    INP;
    OUT;
    SF("%d",&n);
    for(t=1;t<=n;t++)
    {
        cin>>st;
        l=strlen(st);
        ans=0;
        i=0;
        while(i<l)
        {

            if(st[i]=='+')
            {
                while(i<l&&st[i]=='+')
                {
                    i++;
                }
                if(st[i]=='-')
                {
                    while(i<l&&st[i]=='-')
                    {
                        i++;
                    }
                    ans+=2;
                }
            }
            else
            {
                while(i<l&&st[i]=='-')
                {
                    i++;
                }
                ans++;
            }
        }

        PF("Case #%d: %lld\n",t,ans);


    }
    return 0;
}
