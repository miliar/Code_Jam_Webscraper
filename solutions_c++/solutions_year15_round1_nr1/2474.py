#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
using namespace std;
int main(){
    int t;
    cin>>t;
    for(int cas=1;cas<=t;cas++){
        int n,m;
        long long arr[2005];
        cin>>n;
        long long ans1=0,ans2=0;
        long long maxd=0;
        cin>>arr[0];
        for(int i=1;i<n;i++){
            cin>>arr[i];
            if(arr[i]<arr[i-1]){
                long long tmp=arr[i-1]-arr[i];
                ans1+=tmp;
                if(tmp>maxd)maxd=tmp;
            }
        }
        //cout<<maxd<<endl;
        if(maxd!=0){
        for(int i=0;i<n-1;i++){
            if(arr[i]>maxd){
                ans2+=maxd;
            }
            else {
                ans2+=arr[i];
            }
        }
        }
        cout<<"Case #"<<cas<<": "<<ans1<<" "<<ans2<<endl;
        /*
        vector<int> btime;
        int b,n;
        cin>>b>>n;
        int tmp;
        cin>>tmp;
        btime.push_back(tmp);
        int gcdmun=tmp;
        for(int i=1;i<b;i++){

            cin>>tmp;
            btime.push_back(tmp);
            gcdmun=gcd(gcdmun,tmp);
        }

        cout<<gcdmun<<endl;
        int round=0;
        for(int i=0;i<b;i++){
            round+=btime[i]/gcdmun;
        }
        int ans=n%round;
        if(ans==0)ans=round;
        cout<<"Case #"<<cas<<": "<<ans<<endl;
        */
    }
}
