#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("aa.out", "w", stdout);
    int t;
    cin>>t;
    for(int ui=1;ui<=t;ui++){
    	int arr[10000],n;
        cin>>n;
        for(int i=0;i<n;i++) cin>>arr[i];
        int ans1=0,ans2=0;
        int res = 0;
        for(int i=1;i<n;i++){
            if(arr[i]-arr[i-1]<0){
                ans1+=(arr[i-1]-arr[i]);
            }
            res = max(res,arr[i-1]-arr[i]);
        }
        for(int i=0;i<n-1;i++){
            if(arr[i]>=res)ans2+=res;
            else ans2+=arr[i];
        }
        cout<<"Case #"<<ui<<": "<<ans1<<" "<<ans2<<"\n";
    }
    return 0;
}
