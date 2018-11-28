#include<bits/stdc++.h>

using namespace std;

#define ll long long
#define inf 1<<30
#define Mod 10000007
#define dbg(a) printf("%d\n",a);
#define sz(a) (a).size()
int n,m;int a[10002];
int MX;


int main()
{
    int i,j,k,T,cs=0;int ans,n;
    freopen("A-large.in","r",stdin);
    //freopen("A-small-attempt0.in","r",stdin);
    freopen("aout.txt","w",stdout);


    cin>>T;
    char s[10002];
    while(T--)
    {
        scanf("%d %s",&n,&s);int sum=0;ans=0;
        sum+=s[0]-48;
        for(i=1;i<=n;i++)
            if(s[i]>48)
            {
                if(sum>=i)sum+=s[i]-48;
                else
                {
                    ans+=i-sum;
                    sum+=s[i]-48+(i-sum);
                }
            }

        printf("Case #%d: %d\n",++cs,ans);

    }

    return 0;
}

