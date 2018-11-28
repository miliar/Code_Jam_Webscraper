#include<bits/stdc++.h>
using namespace std;

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
#define bitcount    __builtin_popcountll
#define sd(x) scanf("%d",&x)
#define sd2(x,y) scanf("%d %d",&x,&y);
#define slld(x) scanf("%lld",&x)
#define rep(i,x,y) for(i=x;i<y;i++)
#define ss(x) scanf("%s",x)
#define ll long long
#define mp(a,b) make_pair(a,b)
#define F first
#define S second
#define pb(x) push_back(x)
#define MOD 1000000007

string a;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    sd(t);

    for(int q=1;q<=t;q++)
    {
        cin>>a;
        int i,n=a.size();
        int ans=0;
        for(i=n-1;i>=0;i--)
        {
            if(a[i]=='+'&&ans%2==1)
                ans++;
            if(a[i]=='-'&&ans%2==0)
            {
                ans++;
            }
        }
        printf("Case #%d: %d\n",q,ans);
    }


}



