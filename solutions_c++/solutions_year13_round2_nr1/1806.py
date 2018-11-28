#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string>
#include<string.h>
#include<cmath>
#include<map>

using namespace std;

#define MX 100 + 10
#define inf 2000000000

long long int arr[MX],n;

long long int  dp(long long int mote,long long int  pos);

int main()
{
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);

    long long int  mote,t,cc=1,ans;

    cin>>t;

    while(t--)
    {
        cin>>mote>>n;

        for(int i=0; i<n; i++)
        {
            cin>>arr[i];
        }

        sort(arr,arr+n);

        ans = dp(mote,0);

        cout<<"Case #"<<cc++<<": "<<ans<<endl;

    }

    return 0;
}

long long int  dp(long long int  mote,long long int  pos)
{
    if(pos==n) return 0;

    long long int  ret = 0;

    if(mote>arr[pos])
    {
        ret = dp(mote+arr[pos],pos+1);
    }
    else
    {
        long long int  p,q;

        p = dp(mote,pos+1) + 1;
        long long int  cnt = 0;

        if(mote>1)
        {
            while(mote<=arr[pos])
            {
                mote = mote + (mote-1);
                cnt++;
            }

            mote = mote + arr[pos];
        }
        else cnt = inf;

        if(cnt!=inf) q = dp(mote,pos+1) + cnt;
        else q = inf;

        ret = min(p,q);
    }
    return ret;
}
