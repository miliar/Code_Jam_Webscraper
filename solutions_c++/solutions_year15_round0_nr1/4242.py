#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<iomanip>
#include<queue>
#include<map>
#define fl(i,s,n) for(i=s;i<n;i++)
#define flr(i,s,n) for(i=s;i>n;i--)
#define ls(i,s) for(i=0;s[i]!='\0';i++)
#define gi(x) scanf("%lld",&x)
#define pi(x) printf("%d",x)
#define checkline(x) while(x!='\0' && x!='\n')
#define pn printf('\n')
#define ps printf(' ')
#define f_in freopen("input.txt","r",stdin)
#define f_out freopen("output.txt","w",stdout)
#define in(i,j,k) ((j<=i) && (i<k))
#define ull unsigned long long int
#define lli long long int
#define ceil(x,n) (x+n-1)/n
using namespace std;
int main()
{
    //f_in;
    //f_out;
    lli t,n,ans,i,j,nof;
    string shy;
    gi(t);
    fl(j,0,t)
    {
        gi(n);
        ans = 0;
        nof = 0;
        cin>>shy;
        fl(i,0,n+1)
        {
            if(ans >= i)
                ans+=(shy[i]-48);
            else
            {
                nof += (i - ans);
                ans+=(shy[i]-48)+i - ans;
            }
        }
    printf("Case #%lld: %lld\n",j+1,nof);
    }
    return 0;
}
