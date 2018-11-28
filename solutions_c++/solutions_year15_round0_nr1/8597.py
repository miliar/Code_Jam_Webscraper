#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int t;
cin>>t;
for(int x=1;x<=t;x++){
int n;
string s;
cin>>n>>s;
int a[1005];
for(int i=0;i<=n;i++){
a[i]=(int)(s[i]) -48;
}
int ans=0;
int ctr=0;
for(int i=0;i<=n;i++){
if(ctr<i&&a[i]>0){
ans+=(i-ctr);
ctr=i;
}
ctr+=a[i];
}
cout<<"Case #"<<x<<": "<<ans<<endl;
}
return 0;
}
