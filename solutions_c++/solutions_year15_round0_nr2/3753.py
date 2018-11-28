#include<bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define y0 hi1
#define y1 hi2
#define ll long long
#define mp make_pair
#define pb push_back
#define sqr(a) (a)*(a)
#define ld long double
#define all(a) (a).begin(), (a).end()

using namespace std;

const int MX=1001;
const int inf=2000000000;

int f(int a[], int n, int limit)
{
    int ans=0;
    int b[MX]={0};
    int mx=0;
    for(int i=0; i<n; i++)
    {
        b[a[i]]++;
        mx=max(mx, a[i]);
    }
    for(int i=mx; i>limit; i--)
    {
        ans+=b[i]*(i/limit+(i%limit>0)-1);
    }
    return limit+ans;
}

main()
{
    ios_base::sync_with_stdio(0);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin>>T;
    for(int num=1; num<=T; num++)
    {
        cout<<"Case #"<<num<<": ";
        int n;
        cin>>n;
        int a[n];
        int ans=inf;
        int mx=0;
        for(int i=0; i<n; i++)
        {
            cin>>a[i];
            mx=max(mx, a[i]);
        }
        int l=1, r=mx;
        for(int limit=l; limit<=r; limit++)
        {
            ans=min(ans, f(a, n, limit));
            //cout<<limit<<" "<<f(a, n, limit)<<endl;
        }
        cout<<ans<<"\n";
    }
}
