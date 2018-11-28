#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<climits>
#include<stack>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    ll tc,t,i,n,a[1005],mx,tmp,mod,ans,j;
    cin>>tc;
    for(t=1;t<=tc;t++)
    {
        mx=0,ans=LLONG_MAX;
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            mx=max(mx,a[i]);
        }
        for(i=1;i<=mx;i++)
        {
            tmp=i;
            for(j=0;j<n;j++)
            {
                if(a[j]<=i)
                    continue;
                else
                {
                    mod=a[j]-i;
                    //cout<<"***** "<<mod<<endl;
                    tmp+=((mod/i)+1);
                    if(mod%i==0)
                        tmp--;
                }
            }
            //cout<<tmp<<endl;
            ans=min(ans,tmp);
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}