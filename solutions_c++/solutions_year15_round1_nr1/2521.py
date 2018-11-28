#include <bits/stdc++.h>
#define INF         numeric_limits<int>::max()
#define ull         unsigned long long
#define ll          long long
#define vi          vector <ll>
#define pii         pair <ll,ll>
#define pb          push_back
#define NUM(x)      x-'0'
#define TEST        ll t,T;cin>>T;for(t=1;t<=T;t++)
#define X           first
#define Y           second

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);

#ifdef DEBUG
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
#endif // DEBUG

    TEST
    {
            cout<<"Case #"<<t<<": ";
            ll n, ans1=0,ans2=0,m=0;

            cin>>n;
            vi a(n);

            for(ll i=0 ; i<n ; i++)
                cin>>a[i];

            for(ll i=1 ; i<n ; i++)
            {
                if(a[i]<a[i-1])
                    {
                        ans1+=a[i-1]-a[i];
                        m=max(m,(a[i-1]-a[i]));
                    }
            }

            //cerr<<"\n"<<m<<" \n";

            for(ll i=0 ; i<n-1 ; i++)
            {
                ans2+=min(a[i],m);
            }



            cout<<ans1<<" "<<ans2<<endl;


    }
}
