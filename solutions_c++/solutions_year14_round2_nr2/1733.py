#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define fastin std::ios::sync_with_stdio(false);cin.tie(NULL)
#define cout_precision(x) cout<<std::fixed<<setprecision(x)
using namespace std;
#ifdef DEBUG
#include <Debug.h>
#endif
int main()
{
    int t,tc=1,a,b,k;
    cin>>t;
    while(t--)
    {
        cin>>a>>b>>k;
        int ans=0;
        for(int i=0; i<a; i++)
        {
            for(int j=0; j<b; j++)
            {
                if((i&j)<k)
                    ans++;
            }
        }
        cout<<"Case #"<<tc++<<": "<<ans<<"\n";
    }
}
