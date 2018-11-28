/*Krypto...........................jagsxi..........!!! */
/*Google Code Jam Round1A */
#include<bits/stdc++.h>
using namespace std;
int main(){
  freopen("in.txt", "r", stdin);
  freopen("1.txt", "w", stdout);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        int n;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        int ans1=0,ans2=0,mx=0;
        for(int i=1;i<n;i++){
            if(arr[i]-arr[i-1]<0){
                ans1+=(arr[i-1]-arr[i]);
            }
            mx=max(mx,arr[i-1]-arr[i]);
        }
        for(int i=0;i<n-1;i++){
            if(arr[i]>=mx)ans2+=mx;
            else ans2+=arr[i];
        }
        cout<<"Case #"<<z<<": "<<ans1<<" "<<ans2<<"\n";
    }
    return 0;
}
