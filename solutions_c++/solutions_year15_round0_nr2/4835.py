#include <bits/stdc++.h>
using namespace std;
int p[1010];
int main() {
	int t,j,i,x,y,d,k,maxi=0;
cin>>t;
for(k=1;k<=t;k++){
cin>>d;
maxi=0;
for(i=1;i<=d;i++){
cin>>p[i];
if(p[i]>=maxi)
maxi=p[i];
}
int count=0,ans=0,result=0,ma=0;
for(i=1;i<=maxi;i++){
ans=0;ma=0;
for(j=1;j<=d;j++){
if(p[j]>i){
if(p[j]%i==0) x=0; else x=1;
ans=ans+x+ p[j]/i -1;
ma=max(ma,i);
}
else
ma=max(ma,p[j]);
}
ans+=ma;
if(ans<maxi)
maxi=ans;
}
cout<<"Case #"<<k<<": "<<maxi<<endl;
}
	return 0;
}