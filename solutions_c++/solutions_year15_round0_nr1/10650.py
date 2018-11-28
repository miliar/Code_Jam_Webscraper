#include<iostream>
#include<cstdio>
#include<stdlib.h>
#include<cstring>
#include<algorithm>
#include<math.h>

typedef unsigned long long ll;

#define FOR(i,n) for(int i=0;i<n;i++)
#define FORS(i,x,n) for(ll i=x;i<=n;i++)
#define FILL(a,b) memset(a,b,sizeof(a))
using namespace std;



int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    int stand;
    int extra=0;
    int sum=0;
    int smax;
    FOR(j,t)
    {
        cin>>smax;
        char s[smax+1];
        FOR(i,smax+1) cin>>s[i];
        extra=0;
        stand=0;
        int p;
        int ans=0;
        FOR(i,smax+1)
        {
            p=s[i]-'0';
            if(p==0)
            {
                continue;
            }
            else
            {
             if(stand>=i)
                {
                    stand=stand+p;
                }
                else
                {
                    extra=i-stand;
                    ans+=extra;
                    stand=stand+extra+p;
                }
            }
        }
        cout<<"Case #"<<j+1<<": "<<ans<<endl;

    }
}

