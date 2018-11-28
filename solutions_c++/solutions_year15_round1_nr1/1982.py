#include<bits/stdc++.h>
using namespace std;
int arr[1001];
int main(){
    int t,n;
    //ifstream cin("A-large.in");
    //ofstream cout("outs2.txt");
    cin>>t;
    int ans1,ans2;
    for(int tt=1;tt<=t;tt++){
        cin>>n;
        ans1=ans2=0;
        double mdiff=0.0;
        for(int i=0;i<n;i++){
            cin>>arr[i];
            if(i>0&&arr[i]<arr[i-1]){
                ans1+=(arr[i-1]-arr[i]);
                mdiff=max(mdiff,(((arr[i-1]-arr[i])/10.0)));
            }
        }
        int v=floor(mdiff*10.0);
        //cout<<v<<endl;
        for(int i=0;i<(n-1);i++){
            if(arr[i]<=(v))ans2+=arr[i];
            else{
                ans2+=v;
            }
        }


        cout<<"Case #"<<tt<<": "<<ans1<<" "<<ans2<<endl;


    }
    return 0;
}
