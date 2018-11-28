#include<iostream>
#include<queue>
using namespace std;

int arr[1003];

int main(){
    int t;
    cin>>t;
    int cs = 1;
    while(t--){
        int n;
        cin>>n;
        int mx = 0;
        for(int i=0; i<n; i++){
            int x;
            cin>>x;
            arr[i] = x;
            mx = max(arr[i], mx);
        }
        int ans = 1000;
        for(int i=1; i<=mx; i++){
            int temp = 0;
            for(int j=0; j<n; j++){
                temp = temp + (arr[j]-1)/i;
            }
            ans = min(temp+i, ans);
        }
        cout<<"Case #"<<cs++<<": "<<ans<<endl;
    }
}
