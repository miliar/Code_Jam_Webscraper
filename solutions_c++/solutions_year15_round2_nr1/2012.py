#include<bits/stdc++.h>
using namespace std;
int arr[10000000],dp[10000000];
int rev(int n){
    int ans=0,d=0,tmp=n;
    while(tmp>0){
        tmp/=10;
        d++;
    }
    tmp=n;
    while(tmp>0){
        ans=ans*10+tmp%10;
        tmp/=10;
    }
    return ans;
}
long long recur(long long i){
    if(i==1)
    return 1;
    if(i/10==0)
        return i;
    if(i%10==0)
        return recur(i-1)+1;
    if(rev(i)<i)
    return min(recur(rev(i)),recur(i-1))+1;
    return recur(i-1)+1;
}
int main(){
    arr[1]=1;arr[2]=2;
    dp[1]=1;dp[2]=2;
    for(int i=3;i<=1000000;i++){
        arr[i]=arr[i-1]+1;
        if(rev(i)<i and i%10!=0){
            arr[i]=min(arr[i],arr[rev(i)]+1);
        }
        //cout<<i<<" "<<arr[i]<<" "<<recur(i)<<endl;
        //if(i%1000==0)
        //cout<<i<<" "<<arr[i]<<endl;
    }
    int t,n;
    cin>>t;
    for(int x=0;x<t;x++){
        cin>>n;
        cout<<"Case #"<<x+1<<": "<<arr[n]<<endl;
    }
}
