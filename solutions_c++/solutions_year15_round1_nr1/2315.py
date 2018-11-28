#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std;
int main(){
	int t;
    cin>>t;
    int tc=0;
    while(t--){
        printf("Case #%d: ",++tc);
        int n;
        cin>>n;
        int arr[1001];
        for(int i=1;i<=n;i++){
            cin>>arr[i];
        }
        int ans1=0,ans2=0,mx=0;
        for(int i=2;i<=n;i++){
            if(arr[i]-arr[i-1]<0){
                ans1+=(arr[i-1]-arr[i]);
            }
            mx=max(mx,arr[i-1]-arr[i]);
        }
        for(int i=1;i<n;i++){
            if(arr[i]>=mx)ans2+=mx;
            else ans2+=arr[i];
        }
        printf("%d %d\n",ans1,ans2);
    }
}
