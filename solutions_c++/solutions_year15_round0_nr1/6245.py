#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	ll t;
    char array[100000];
    ll smax;
    cin>>t;
    ll running,ans;
    ll j=1;
   for(ll l=1;l<=t;l++)
    {
        running=0;
        ans=0;
        cin>>smax;
        cin>>array;
        for(ll i=0;i<smax+1;i++)
        {
            if(running<i)
            {
                ans+=(i-running);
                //printf("%d res\n",ans);
                running+=(i-running)+array[i]-48;
            }
            else
            {
                running+=(array[i]-48);
            }
        }
        printf("Case #%lld: %lld\n",l,ans);
    }

	return 0;
}
