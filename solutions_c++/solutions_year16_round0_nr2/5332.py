#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
#define f first
#define s second
#define si(x)   scanf("%d",&x)
#define sl(x)   scanf("%I64d",&x)
#define CLR(x)  memset(x,0,sizeof(x))
#define RESET(x,a) memset(x,a,sizeof(x))
#define pi pair<int,int>
#define pb push_back
#define mp make_pair
#define debug(x) cerr<<">value ("<<#x<<") : "<<x<<endl;

char s[130];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-out.txt","w",stdout);
    int tt,t,n,m,i,j,ans;
    si(tt);
    for(t=1;t<=tt;t++)
    {
        scanf("%s",s);
        n=strlen(s);
        while(n&&s[n-1]=='+')
            n--;
        if(n<=0)
        {
            printf("Case #%d: 0\n",t);
            continue;
        }
        ans=i=0;
        while(i<n&&s[i]=='+')
            i++;
        if(i!=0)
            ans=1;
        while(i<n)
        {
            while(i<n&&s[i]=='-')
				i++;
            if(i>=n)
                break;
            while(i<n&&s[i]=='+')
				i++;
            ans+=2;
        }
        printf("Case #%d: %d\n",t,ans+1);
    }
    return 0;
}

