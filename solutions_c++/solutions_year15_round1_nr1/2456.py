#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <cstdlib>
#include <cstdio>


using namespace std;

int main(){
    int t,i,j=1,n,a[100005];
    cin>>t;
    while(t--){
        cin>>n;

        for(i=0;i<n;i++)
            cin>>a[i];

        int ans=0,ans2=0,mx=0;
        for(i=1;i<=n-1;i++)
		{
            int diff=a[i-1]-a[i];
			if(diff>=0) ans+=diff;
            mx=max(mx,diff);
        }
        for(i=0;i<n-1;i++)
		{
            if(a[i]>=mx) ans2+=mx;
            else ans2+=a[i];
        }
        cout<<"Case #"<<j++<<": "<<ans<<" "<<ans2<<"\n";

    }
    return 0;
}
