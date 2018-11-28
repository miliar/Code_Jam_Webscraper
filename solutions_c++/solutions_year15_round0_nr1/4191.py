//ABHAY GARG
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mod 1000000007LL
#define mp make_pair
int main()
{
    //freopen("inp.in","r",stdin);
    //freopen("oup.txt","w",stdout);
    int i,j,k,a[100001],c=1,t,ans,n,d;
    char s[100001];
    scanf("%d",&t);
    while(t--)
    {
        cin>>n>>s;
        for(i=0;i<=n;i++)
            a[i]=s[i]-'0';
        ans=0;
        d=a[0];
        for(i=1;i<=n;i++)
            if(d>=i)
                d=d+a[i];
            else
            {
                ans=ans+(i-d);
                d=i+a[i];
            }
        assert(ans>=0&&ans<=n);
        printf("Case #%d: %d\n",c,ans);
        c++;
    }
    return 0;
}
