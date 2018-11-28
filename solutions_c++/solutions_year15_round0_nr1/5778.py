#include <bits/stdc++.h>
#define INF         0x7fffffff
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
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    TEST
    {
        int n;
        string s;

        cin>>n>>s;
        n++;

        vi a(n);

        for(int i=0 ; i<n ; i++)
            a[i] = NUM(s[i]);

        ll x=0, y=0;

        for(int i=0 ; i<n ; i++)
        {

            if(x+y>=i)
                y+=a[i];
            else if(a[i])
                x=(i--)-y;
        }

    cout<<"Case #"<<t<<": "<<x<<endl;
    }

}
