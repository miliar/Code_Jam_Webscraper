#include <bits/stdc++.h>
#define sflld(n) scanf("%lld",&n)
#define sfulld(n) scanf("%llu",&n)
#define sfd(n) scanf("%d",&n)
#define sfld(n) scanf("%ld",&n)
#define sfs(n) scanf("%s",&n)
#define ll long long
#define ull unsigned long long int
#define pflld(n) printf("%lld\n",n)
#define pfd(n) printf("%d\n",n)
#define pfld(n) printf("%ld\n",n)
using namespace std;

int main()
{
    int t,s,i,ct,ans,j=1;
    char a[1005];
    sfd(t);
    while(j<=t)
    {
        sfd(s);
        ct=0;
        ans=0;
        sfs(a);
        //cout<<a<<endl;
        for(i=0;i<=s;i++)
        {

            if(ct>=i)
            {
                ct+=(a[i]-48);
            }
            else
            {
                ans+=i-ct;
                ct+=i-ct+(a[i]-48);
            }
        }
        cout<<"Case #"<<j<<": "<<ans<<endl;
        j++;

    }
    return 0;
}
