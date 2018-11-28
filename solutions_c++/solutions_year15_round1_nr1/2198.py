#include<iostream>
using namespace std;
int main(){
long long int arr[10001],ans,maxn,T;
cin>>T;
for(int i=1;i<=T;i++){
int N;
ans=0;
maxn=0;
cout<<"Case #"<<i<<": ";
cin>>N;
cin>>arr[0];
for(int j=1;j<N;j++){
cin>>arr[j];

maxn=(arr[j-1]-arr[j])>maxn?(arr[j-1]-arr[j]):maxn;
if(arr[j]<arr[j-1]){
ans=ans+arr[j-1]-arr[j];
}
}
cout<<ans<<" ";
ans=0;
for(int j=0;j<N-1;j++){
ans+=min(maxn,arr[j]);
}
cout<<ans<<endl;
}
return 0;
}